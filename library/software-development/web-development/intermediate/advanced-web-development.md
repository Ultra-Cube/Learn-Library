# 🏆 **Advanced Web Development with React & Node.js**

## Advanced Web Development with React & Node.js

*Build modern full-stack applications with professional architecture patterns*

## 📚 **Lesson Overview**

**Duration**: 75 minutes  
**Level**: Intermediate  
**Prerequisites**: Programming Fundamentals, HTML/CSS/JavaScript basics  
**Learning Path**: Software Development → Web Development → Advanced Web Development

---

## 🎯 **Learning Objectives**

By the end of this lesson, you will be able to:

- ✅ Build scalable React applications with modern hooks and state management
- ✅ Create RESTful APIs with Node.js, Express, and MongoDB
- ✅ Implement authentication, authorization, and security best practices
- ✅ Deploy full-stack applications to cloud platforms with CI/CD
- ✅ Apply advanced patterns like microservices and serverless architecture

---

## 🌟 **Why This Matters**

Full-stack web development is one of the most in-demand skills in technology. **React powers 40%+ of modern web applications**, including Facebook, Netflix, and Airbnb. **Node.js handles 85% of real-time applications** and is used by NASA, LinkedIn, and Uber. According to **Stack Overflow 2024**, full-stack developers earn an average of **$120,000-$180,000** annually.

> *"The future belongs to full-stack developers who can build complete solutions."* - **Dan Abramov, React Core Team**

**Industry Impact:**

- **Netflix**: React-based interface serves 230M+ users globally
- **WhatsApp**: Node.js handles 2B+ messages daily with minimal servers
- **Airbnb**: Full-stack architecture processes $38B+ in bookings annually

---

## 📖 **Core Content**

### **Part 1: Advanced React Development (25 minutes)**

#### **⚛️ Modern React Architecture**

```jsx
// Advanced React component architecture with hooks
import React, { useState, useEffect, useContext, useCallback, useMemo } from 'react';
import { useQuery, useMutation, useQueryClient } from 'react-query';
import { useAuth } from '../hooks/useAuth';
import { TaskService } from '../services/taskService';

// Context for global state management
const TaskContext = React.createContext();

// Custom hook for task management
const useTasks = () => {
  const context = useContext(TaskContext);
  if (!context) {
    throw new Error('useTasks must be used within TaskProvider');
  }
  return context;
};

// Advanced component with performance optimization
const TaskDashboard = React.memo(() => {
  const { user } = useAuth();
  const queryClient = useQueryClient();
  
  // React Query for server state management
  const {
    data: tasks,
    isLoading,
    error,
    refetch
  } = useQuery(['tasks', user.id], () => TaskService.getTasks(user.id), {
    staleTime: 5 * 60 * 1000, // 5 minutes
    cacheTime: 10 * 60 * 1000, // 10 minutes
    retry: 3,
    retryDelay: attemptIndex => Math.min(1000 * 2 ** attemptIndex, 30000)
  });

  // Optimistic updates with mutations
  const createTaskMutation = useMutation(TaskService.createTask, {
    onMutate: async (newTask) => {
      await queryClient.cancelQueries(['tasks', user.id]);
      const previousTasks = queryClient.getQueryData(['tasks', user.id]);
      
      queryClient.setQueryData(['tasks', user.id], (old) => [
        ...old,
        { ...newTask, id: Date.now(), status: 'pending' }
      ]);
      
      return { previousTasks };
    },
    onError: (err, newTask, context) => {
      queryClient.setQueryData(['tasks', user.id], context.previousTasks);
    },
    onSettled: () => {
      queryClient.invalidateQueries(['tasks', user.id]);
    }
  });

  // Memoized calculations for performance
  const taskStats = useMemo(() => {
    if (!tasks) return { total: 0, completed: 0, pending: 0 };
    
    return tasks.reduce((stats, task) => {
      stats.total++;
      stats[task.status]++;
      return stats;
    }, { total: 0, completed: 0, pending: 0 });
  }, [tasks]);

  // Debounced search functionality
  const [searchTerm, setSearchTerm] = useState('');
  const [debouncedSearchTerm, setDebouncedSearchTerm] = useState('');

  useEffect(() => {
    const timer = setTimeout(() => {
      setDebouncedSearchTerm(searchTerm);
    }, 300);

    return () => clearTimeout(timer);
  }, [searchTerm]);

  // Filtered tasks based on search
  const filteredTasks = useMemo(() => {
    if (!tasks) return [];
    if (!debouncedSearchTerm) return tasks;
    
    return tasks.filter(task =>
      task.title.toLowerCase().includes(debouncedSearchTerm.toLowerCase()) ||
      task.description.toLowerCase().includes(debouncedSearchTerm.toLowerCase())
    );
  }, [tasks, debouncedSearchTerm]);

  const handleCreateTask = useCallback((taskData) => {
    createTaskMutation.mutate({
      ...taskData,
      userId: user.id,
      createdAt: new Date().toISOString()
    });
  }, [createTaskMutation, user.id]);

  if (isLoading) return <TaskSkeleton />;
  if (error) return <ErrorBoundary error={error} onRetry={refetch} />;

  return (
    <div className="task-dashboard">
      <DashboardHeader stats={taskStats} />
      
      <div className="task-controls">
        <SearchInput
          value={searchTerm}
          onChange={setSearchTerm}
          placeholder="Search tasks..."
        />
        <CreateTaskButton onClick={handleCreateTask} />
      </div>

      <TaskGrid
        tasks={filteredTasks}
        onTaskUpdate={(taskId, updates) => {
          // Optimistic update logic
        }}
        onTaskDelete={(taskId) => {
          // Optimistic delete logic
        }}
      />

      <TaskAnalytics tasks={tasks} />
    </div>
  );
});

// Performance-optimized task item component
const TaskItem = React.memo(({ task, onUpdate, onDelete }) => {
  const [isEditing, setIsEditing] = useState(false);
  const [optimisticTask, setOptimisticTask] = useState(task);

  // Optimistic UI updates
  const handleStatusChange = useCallback((newStatus) => {
    setOptimisticTask(prev => ({ ...prev, status: newStatus }));
    onUpdate(task.id, { status: newStatus });
  }, [task.id, onUpdate]);

  return (
    <div className={`task-item ${optimisticTask.status}`}>
      <div className="task-header">
        <h3>{optimisticTask.title}</h3>
        <TaskActions
          task={optimisticTask}
          onEdit={() => setIsEditing(true)}
          onDelete={() => onDelete(task.id)}
          onStatusChange={handleStatusChange}
        />
      </div>
      
      {isEditing ? (
        <TaskEditor
          task={optimisticTask}
          onSave={(updates) => {
            setOptimisticTask(prev => ({ ...prev, ...updates }));
            onUpdate(task.id, updates);
            setIsEditing(false);
          }}
          onCancel={() => setIsEditing(false)}
        />
      ) : (
        <TaskDisplay task={optimisticTask} />
      )}
    </div>
  );
}, (prevProps, nextProps) => {
  // Custom comparison for memo optimization
  return (
    prevProps.task.id === nextProps.task.id &&
    prevProps.task.status === nextProps.task.status &&
    prevProps.task.updatedAt === nextProps.task.updatedAt
  );
});

// Advanced state management with useReducer
const taskReducer = (state, action) => {
  switch (action.type) {
    case 'LOAD_TASKS':
      return {
        ...state,
        tasks: action.payload,
        loading: false,
        error: null
      };
    
    case 'ADD_TASK':
      return {
        ...state,
        tasks: [...state.tasks, action.payload],
        totalCount: state.totalCount + 1
      };
    
    case 'UPDATE_TASK':
      return {
        ...state,
        tasks: state.tasks.map(task =>
          task.id === action.payload.id
            ? { ...task, ...action.payload.updates }
            : task
        )
      };
    
    case 'DELETE_TASK':
      return {
        ...state,
        tasks: state.tasks.filter(task => task.id !== action.payload),
        totalCount: state.totalCount - 1
      };
    
    case 'SET_FILTER':
      return {
        ...state,
        filter: action.payload,
        filteredTasks: filterTasks(state.tasks, action.payload)
      };
    
    default:
      return state;
  }
};

// Context provider with advanced state management
export const TaskProvider = ({ children }) => {
  const [state, dispatch] = useReducer(taskReducer, {
    tasks: [],
    filteredTasks: [],
    loading: true,
    error: null,
    filter: 'all',
    totalCount: 0
  });

  const value = {
    ...state,
    dispatch
  };

  return (
    <TaskContext.Provider value={value}>
      {children}
    </TaskContext.Provider>
  );
};
```

#### **🎯 Advanced React Patterns**

```jsx
// Higher-Order Components (HOC) for reusability
const withAuthentication = (WrappedComponent) => {
  return function AuthenticatedComponent(props) {
    const { user, isLoading } = useAuth();
    
    if (isLoading) return <LoadingSpinner />;
    if (!user) return <LoginForm />;
    
    return <WrappedComponent {...props} user={user} />;
  };
};

// Render Props pattern for flexible components
const DataFetcher = ({ url, children }) => {
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchData = async () => {
      try {
        setLoading(true);
        const response = await fetch(url);
        const result = await response.json();
        setData(result);
      } catch (err) {
        setError(err);
      } finally {
        setLoading(false);
      }
    };

    fetchData();
  }, [url]);

  return children({ data, loading, error });
};

// Usage of render props
const TaskList = () => (
  <DataFetcher url="/api/tasks">
    {({ data: tasks, loading, error }) => {
      if (loading) return <LoadingSpinner />;
      if (error) return <ErrorMessage error={error} />;
      return (
        <div>
          {tasks.map(task => (
            <TaskItem key={task.id} task={task} />
          ))}
        </div>
      );
    }}
  </DataFetcher>
);

// Custom hooks for business logic
const useLocalStorage = (key, initialValue) => {
  const [storedValue, setStoredValue] = useState(() => {
    try {
      const item = window.localStorage.getItem(key);
      return item ? JSON.parse(item) : initialValue;
    } catch (error) {
      console.error(`Error reading localStorage key "${key}":`, error);
      return initialValue;
    }
  });

  const setValue = useCallback((value) => {
    try {
      const valueToStore = value instanceof Function ? value(storedValue) : value;
      setStoredValue(valueToStore);
      window.localStorage.setItem(key, JSON.stringify(valueToStore));
    } catch (error) {
      console.error(`Error setting localStorage key "${key}":`, error);
    }
  }, [key, storedValue]);

  return [storedValue, setValue];
};

// Advanced form handling with validation
const useForm = (initialValues, validationSchema) => {
  const [values, setValues] = useState(initialValues);
  const [errors, setErrors] = useState({});
  const [touched, setTouched] = useState({});
  const [isSubmitting, setIsSubmitting] = useState(false);

  const validate = useCallback((fieldValues = values) => {
    const newErrors = {};
    
    Object.keys(validationSchema).forEach(field => {
      const value = fieldValues[field];
      const rules = validationSchema[field];
      
      if (rules.required && (!value || value.toString().trim() === '')) {
        newErrors[field] = `${field} is required`;
        return;
      }
      
      if (rules.minLength && value.length < rules.minLength) {
        newErrors[field] = `${field} must be at least ${rules.minLength} characters`;
        return;
      }
      
      if (rules.pattern && !rules.pattern.test(value)) {
        newErrors[field] = rules.message || `${field} format is invalid`;
        return;
      }
      
      if (rules.custom) {
        const customError = rules.custom(value, fieldValues);
        if (customError) {
          newErrors[field] = customError;
          return;
        }
      }
    });
    
    setErrors(newErrors);
    return Object.keys(newErrors).length === 0;
  }, [values, validationSchema]);

  const handleChange = useCallback((name, value) => {
    setValues(prev => ({ ...prev, [name]: value }));
    
    if (touched[name]) {
      validate({ ...values, [name]: value });
    }
  }, [values, touched, validate]);

  const handleBlur = useCallback((name) => {
    setTouched(prev => ({ ...prev, [name]: true }));
    validate();
  }, [validate]);

  const handleSubmit = useCallback(async (onSubmit) => {
    const allTouched = Object.keys(values).reduce((acc, key) => {
      acc[key] = true;
      return acc;
    }, {});
    
    setTouched(allTouched);
    
    if (validate()) {
      setIsSubmitting(true);
      try {
        await onSubmit(values);
      } catch (error) {
        console.error('Form submission error:', error);
      } finally {
        setIsSubmitting(false);
      }
    }
  }, [values, validate]);

  return {
    values,
    errors,
    touched,
    isSubmitting,
    handleChange,
    handleBlur,
    handleSubmit,
    resetForm: () => {
      setValues(initialValues);
      setErrors({});
      setTouched({});
      setIsSubmitting(false);
    }
  };
};
```

### **Part 2: Backend API Development with Node.js (25 minutes)**

#### **🚀 Professional Node.js API Architecture**

```javascript
// Advanced Express.js API with middleware architecture
const express = require('express');
const mongoose = require('mongoose');
const helmet = require('helmet');
const cors = require('cors');
const rateLimit = require('express-rate-limit');
const compression = require('compression');
const morgan = require('morgan');
const { body, validationResult } = require('express-validator');
const jwt = require('jsonwebtoken');
const bcrypt = require('bcryptjs');
const Redis = require('redis');

// Initialize Express app
const app = express();
const redis = Redis.createClient();

// Security middleware
app.use(helmet({
  contentSecurityPolicy: {
    directives: {
      defaultSrc: ["'self'"],
      styleSrc: ["'self'", "'unsafe-inline'"],
      scriptSrc: ["'self'"],
      imgSrc: ["'self'", "data:", "https:"],
    },
  },
  hsts: {
    maxAge: 31536000,
    includeSubDomains: true,
    preload: true
  }
}));

// Rate limiting
const limiter = rateLimit({
  windowMs: 15 * 60 * 1000, // 15 minutes
  max: 100, // limit each IP to 100 requests per windowMs
  message: {
    error: 'Too many requests from this IP, please try again later.',
    retryAfter: '15 minutes'
  },
  standardHeaders: true,
  legacyHeaders: false,
});

app.use('/api/', limiter);

// CORS configuration
app.use(cors({
  origin: process.env.NODE_ENV === 'production' 
    ? ['https://yourdomain.com', 'https://www.yourdomain.com']
    : ['http://localhost:3000', 'http://localhost:3001'],
  credentials: true,
  methods: ['GET', 'POST', 'PUT', 'DELETE', 'PATCH'],
  allowedHeaders: ['Content-Type', 'Authorization']
}));

// Body parsing and compression
app.use(express.json({ limit: '10mb' }));
app.use(express.urlencoded({ extended: true, limit: '10mb' }));
app.use(compression());

// Logging
app.use(morgan('combined'));

// Database connection with monitoring
mongoose.connect(process.env.MONGODB_URI, {
  useNewUrlParser: true,
  useUnifiedTopology: true,
  maxPoolSize: 10,
  serverSelectionTimeoutMS: 5000,
  socketTimeoutMS: 45000,
});

mongoose.connection.on('connected', () => {
  console.log('✅ MongoDB connected successfully');
});

mongoose.connection.on('error', (err) => {
  console.error('❌ MongoDB connection error:', err);
});

// Advanced Mongoose schema with validation and middleware
const taskSchema = new mongoose.Schema({
  title: {
    type: String,
    required: [true, 'Task title is required'],
    trim: true,
    maxlength: [100, 'Title cannot exceed 100 characters']
  },
  description: {
    type: String,
    trim: true,
    maxlength: [500, 'Description cannot exceed 500 characters']
  },
  status: {
    type: String,
    enum: {
      values: ['pending', 'in-progress', 'completed', 'cancelled'],
      message: '{VALUE} is not a valid status'
    },
    default: 'pending'
  },
  priority: {
    type: String,
    enum: ['low', 'medium', 'high', 'urgent'],
    default: 'medium'
  },
  dueDate: {
    type: Date,
    validate: {
      validator: function(value) {
        return !value || value > new Date();
      },
      message: 'Due date must be in the future'
    }
  },
  assignedTo: {
    type: mongoose.Schema.Types.ObjectId,
    ref: 'User',
    required: true
  },
  createdBy: {
    type: mongoose.Schema.Types.ObjectId,
    ref: 'User',
    required: true
  },
  tags: [{
    type: String,
    trim: true,
    lowercase: true
  }],
  attachments: [{
    filename: String,
    originalname: String,
    mimetype: String,
    size: Number,
    url: String
  }],
  estimatedHours: {
    type: Number,
    min: [0, 'Estimated hours cannot be negative'],
    max: [1000, 'Estimated hours cannot exceed 1000']
  },
  actualHours: {
    type: Number,
    min: [0, 'Actual hours cannot be negative']
  }
}, {
  timestamps: true,
  toJSON: { virtuals: true },
  toObject: { virtuals: true }
});

// Virtual fields
taskSchema.virtual('isOverdue').get(function() {
  return this.dueDate && this.dueDate < new Date() && this.status !== 'completed';
});

taskSchema.virtual('timeRemaining').get(function() {
  if (!this.dueDate) return null;
  const now = new Date();
  const remaining = this.dueDate - now;
  return remaining > 0 ? remaining : 0;
});

// Indexes for performance
taskSchema.index({ assignedTo: 1, status: 1 });
taskSchema.index({ createdBy: 1, createdAt: -1 });
taskSchema.index({ dueDate: 1, status: 1 });
taskSchema.index({ tags: 1 });

// Middleware hooks
taskSchema.pre('save', function(next) {
  if (this.isModified('status') && this.status === 'completed') {
    this.completedAt = new Date();
  }
  next();
});

taskSchema.post('save', async function(doc) {
  // Emit real-time update
  const io = require('../socket');
  io.to(`user:${doc.assignedTo}`).emit('taskUpdated', doc);
  
  // Update cache
  await redis.del(`tasks:user:${doc.assignedTo}`);
});

const Task = mongoose.model('Task', taskSchema);

// Authentication middleware
const authenticateToken = async (req, res, next) => {
  const authHeader = req.headers['authorization'];
  const token = authHeader && authHeader.split(' ')[1];

  if (!token) {
    return res.status(401).json({
      success: false,
      message: 'Access token required'
    });
  }

  try {
    // Check if token is blacklisted
    const blacklisted = await redis.get(`blacklist:${token}`);
    if (blacklisted) {
      return res.status(401).json({
        success: false,
        message: 'Token has been revoked'
      });
    }

    const decoded = jwt.verify(token, process.env.JWT_SECRET);
    
    // Get user from cache or database
    let user = await redis.get(`user:${decoded.userId}`);
    if (user) {
      user = JSON.parse(user);
    } else {
      user = await User.findById(decoded.userId).select('-password');
      if (user) {
        await redis.setex(`user:${decoded.userId}`, 300, JSON.stringify(user)); // 5 min cache
      }
    }

    if (!user) {
      return res.status(401).json({
        success: false,
        message: 'Invalid token'
      });
    }

    req.user = user;
    next();
  } catch (error) {
    return res.status(403).json({
      success: false,
      message: 'Invalid or expired token'
    });
  }
};

// Validation middleware
const validateTask = [
  body('title')
    .trim()
    .isLength({ min: 1, max: 100 })
    .withMessage('Title must be between 1 and 100 characters'),
  
  body('description')
    .optional()
    .trim()
    .isLength({ max: 500 })
    .withMessage('Description cannot exceed 500 characters'),
  
  body('status')
    .optional()
    .isIn(['pending', 'in-progress', 'completed', 'cancelled'])
    .withMessage('Invalid status value'),
  
  body('priority')
    .optional()
    .isIn(['low', 'medium', 'high', 'urgent'])
    .withMessage('Invalid priority value'),
  
  body('dueDate')
    .optional()
    .isISO8601()
    .toDate()
    .custom((value) => {
      if (value && value <= new Date()) {
        throw new Error('Due date must be in the future');
      }
      return true;
    }),
  
  body('estimatedHours')
    .optional()
    .isFloat({ min: 0, max: 1000 })
    .withMessage('Estimated hours must be between 0 and 1000'),

  (req, res, next) => {
    const errors = validationResult(req);
    if (!errors.isEmpty()) {
      return res.status(400).json({
        success: false,
        message: 'Validation failed',
        errors: errors.array()
      });
    }
    next();
  }
];

// Advanced API endpoints with caching and error handling
class TaskController {
  // Get tasks with advanced filtering, sorting, and pagination
  static async getTasks(req, res) {
    try {
      const {
        page = 1,
        limit = 10,
        status,
        priority,
        assignedTo,
        search,
        sortBy = 'createdAt',
        sortOrder = 'desc',
        startDate,
        endDate
      } = req.query;

      // Build cache key
      const cacheKey = `tasks:${JSON.stringify(req.query)}:user:${req.user._id}`;
      
      // Check cache first
      const cached = await redis.get(cacheKey);
      if (cached) {
        return res.json({
          success: true,
          data: JSON.parse(cached),
          cached: true
        });
      }

      // Build query
      const query = { 
        $or: [
          { assignedTo: req.user._id },
          { createdBy: req.user._id }
        ]
      };

      if (status) query.status = status;
      if (priority) query.priority = priority;
      if (assignedTo) query.assignedTo = assignedTo;

      if (search) {
        query.$and = [
          query.$or ? { $or: query.$or } : {},
          {
            $or: [
              { title: { $regex: search, $options: 'i' } },
              { description: { $regex: search, $options: 'i' } },
              { tags: { $in: [new RegExp(search, 'i')] } }
            ]
          }
        ];
        delete query.$or;
      }

      if (startDate || endDate) {
        query.createdAt = {};
        if (startDate) query.createdAt.$gte = new Date(startDate);
        if (endDate) query.createdAt.$lte = new Date(endDate);
      }

      // Execute query with pagination
      const skip = (parseInt(page) - 1) * parseInt(limit);
      const sortOptions = { [sortBy]: sortOrder === 'desc' ? -1 : 1 };

      const [tasks, totalCount] = await Promise.all([
        Task.find(query)
          .populate('assignedTo', 'name email avatar')
          .populate('createdBy', 'name email')
          .sort(sortOptions)
          .skip(skip)
          .limit(parseInt(limit))
          .lean(),
        Task.countDocuments(query)
      ]);

      const result = {
        tasks,
        pagination: {
          currentPage: parseInt(page),
          totalPages: Math.ceil(totalCount / parseInt(limit)),
          totalCount,
          hasNext: skip + tasks.length < totalCount,
          hasPrev: parseInt(page) > 1
        }
      };

      // Cache for 5 minutes
      await redis.setex(cacheKey, 300, JSON.stringify(result));

      res.json({
        success: true,
        data: result
      });

    } catch (error) {
      console.error('Get tasks error:', error);
      res.status(500).json({
        success: false,
        message: 'Failed to retrieve tasks',
        error: process.env.NODE_ENV === 'development' ? error.message : 'Internal server error'
      });
    }
  }

  // Create task with transaction support
  static async createTask(req, res) {
    const session = await mongoose.startSession();
    session.startTransaction();

    try {
      const taskData = {
        ...req.body,
        createdBy: req.user._id,
        assignedTo: req.body.assignedTo || req.user._id
      };

      const task = new Task(taskData);
      await task.save({ session });

      // Create activity log
      const ActivityLog = mongoose.model('ActivityLog');
      await ActivityLog.create([{
        action: 'task_created',
        entityType: 'Task',
        entityId: task._id,
        userId: req.user._id,
        metadata: {
          taskTitle: task.title,
          assignedTo: task.assignedTo
        }
      }], { session });

      await session.commitTransaction();

      // Populate and return
      await task.populate('assignedTo', 'name email avatar');
      await task.populate('createdBy', 'name email');

      // Clear relevant caches
      await redis.del(`tasks:user:${task.assignedTo}`);
      await redis.del(`tasks:user:${task.createdBy}`);

      res.status(201).json({
        success: true,
        data: task,
        message: 'Task created successfully'
      });

    } catch (error) {
      await session.abortTransaction();
      console.error('Create task error:', error);
      
      if (error.name === 'ValidationError') {
        return res.status(400).json({
          success: false,
          message: 'Validation failed',
          errors: Object.values(error.errors).map(e => e.message)
        });
      }

      res.status(500).json({
        success: false,
        message: 'Failed to create task',
        error: process.env.NODE_ENV === 'development' ? error.message : 'Internal server error'
      });
    } finally {
      session.endSession();
    }
  }

  // Update task with optimistic locking
  static async updateTask(req, res) {
    try {
      const { id } = req.params;
      const updates = req.body;

      // Check if user has permission to update
      const task = await Task.findById(id);
      if (!task) {
        return res.status(404).json({
          success: false,
          message: 'Task not found'
        });
      }

      const canUpdate = task.assignedTo.toString() === req.user._id.toString() ||
                       task.createdBy.toString() === req.user._id.toString() ||
                       req.user.role === 'admin';

      if (!canUpdate) {
        return res.status(403).json({
          success: false,
          message: 'Insufficient permissions to update this task'
        });
      }

      // Optimistic locking check
      if (updates.version && task.version !== updates.version) {
        return res.status(409).json({
          success: false,
          message: 'Task has been modified by another user. Please refresh and try again.'
        });
      }

      // Update task
      Object.assign(task, updates);
      task.version = (task.version || 0) + 1;
      await task.save();

      await task.populate('assignedTo', 'name email avatar');
      await task.populate('createdBy', 'name email');

      // Clear caches
      await redis.del(`tasks:user:${task.assignedTo}`);
      await redis.del(`tasks:user:${task.createdBy}`);

      res.json({
        success: true,
        data: task,
        message: 'Task updated successfully'
      });

    } catch (error) {
      console.error('Update task error:', error);
      res.status(500).json({
        success: false,
        message: 'Failed to update task',
        error: process.env.NODE_ENV === 'development' ? error.message : 'Internal server error'
      });
    }
  }
}

// API Routes with proper RESTful design
const router = express.Router();

router.get('/tasks', authenticateToken, TaskController.getTasks);
router.post('/tasks', authenticateToken, validateTask, TaskController.createTask);
router.put('/tasks/:id', authenticateToken, validateTask, TaskController.updateTask);
router.delete('/tasks/:id', authenticateToken, TaskController.deleteTask);
router.get('/tasks/:id', authenticateToken, TaskController.getTask);

// Health check endpoint
router.get('/health', (req, res) => {
  res.json({
    status: 'healthy',
    timestamp: new Date().toISOString(),
    uptime: process.uptime(),
    memory: process.memoryUsage(),
    version: process.env.npm_package_version
  });
});

app.use('/api/v1', router);

// Global error handler
app.use((error, req, res, next) => {
  console.error('Global error handler:', error);
  
  res.status(error.status || 500).json({
    success: false,
    message: error.message || 'Internal server error',
    ...(process.env.NODE_ENV === 'development' && { stack: error.stack })
  });
});

// 404 handler
app.use('*', (req, res) => {
  res.status(404).json({
    success: false,
    message: 'API endpoint not found'
  });
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`🚀 Server running on port ${PORT}`);
});

module.exports = app;
```

### **Part 3: Database Design & Security (15 minutes)**

#### **🗄️ Advanced MongoDB & Security**

```javascript
// Advanced database design and security patterns

// Database schema design with relationships
const userSchema = new mongoose.Schema({
  name: {
    type: String,
    required: true,
    trim: true,
    maxlength: 50
  },
  email: {
    type: String,
    required: true,
    unique: true,
    lowercase: true,
    validate: {
      validator: function(email) {
        return /^\w+([.-]?\w+)*@\w+([.-]?\w+)*(\.\w{2,3})+$/.test(email);
      },
      message: 'Please enter a valid email'
    }
  },
  password: {
    type: String,
    required: true,
    minlength: 8,
    validate: {
      validator: function(password) {
        // At least one uppercase, one lowercase, one number, one special char
        return /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]/.test(password);
      },
      message: 'Password must contain at least one uppercase letter, one lowercase letter, one number, and one special character'
    }
  },
  role: {
    type: String,
    enum: ['user', 'admin', 'manager'],
    default: 'user'
  },
  profile: {
    avatar: String,
    bio: { type: String, maxlength: 200 },
    department: String,
    position: String,
    phoneNumber: {
      type: String,
      validate: {
        validator: function(phone) {
          return !phone || /^\+?[\d\s\-\(\)]+$/.test(phone);
        },
        message: 'Please enter a valid phone number'
      }
    }
  },
  preferences: {
    notifications: {
      email: { type: Boolean, default: true },
      push: { type: Boolean, default: true },
      sms: { type: Boolean, default: false }
    },
    theme: {
      type: String,
      enum: ['light', 'dark', 'auto'],
      default: 'light'
    },
    language: {
      type: String,
      default: 'en'
    }
  },
  security: {
    lastLogin: Date,
    loginAttempts: { type: Number, default: 0 },
    lockUntil: Date,
    passwordResetToken: String,
    passwordResetExpires: Date,
    emailVerificationToken: String,
    emailVerified: { type: Boolean, default: false },
    twoFactorSecret: String,
    twoFactorEnabled: { type: Boolean, default: false }
  },
  isActive: { type: Boolean, default: true }
}, {
  timestamps: true,
  toJSON: { 
    virtuals: true,
    transform: function(doc, ret) {
      delete ret.password;
      delete ret.security.passwordResetToken;
      delete ret.security.twoFactorSecret;
      return ret;
    }
  }
});

// Virtual for account lock status
userSchema.virtual('isLocked').get(function() {
  return !!(this.security.lockUntil && this.security.lockUntil > Date.now());
});

// Password hashing middleware
userSchema.pre('save', async function(next) {
  if (!this.isModified('password')) return next();
  
  try {
    const salt = await bcrypt.genSalt(12);
    this.password = await bcrypt.hash(this.password, salt);
    next();
  } catch (error) {
    next(error);
  }
});

// Password comparison method
userSchema.methods.comparePassword = async function(candidatePassword) {
  if (this.isLocked) {
    throw new Error('Account is temporarily locked');
  }
  
  const isMatch = await bcrypt.compare(candidatePassword, this.password);
  
  if (!isMatch) {
    this.security.loginAttempts += 1;
    
    // Lock account after 5 failed attempts for 30 minutes
    if (this.security.loginAttempts >= 5) {
      this.security.lockUntil = Date.now() + 30 * 60 * 1000; // 30 minutes
    }
    
    await this.save();
    throw new Error('Invalid password');
  }
  
  // Reset login attempts on successful login
  if (this.security.loginAttempts > 0) {
    this.security.loginAttempts = 0;
    this.security.lockUntil = undefined;
  }
  
  this.security.lastLogin = new Date();
  await this.save();
  
  return true;
};

// JWT token generation
userSchema.methods.generateAuthToken = function() {
  const payload = {
    userId: this._id,
    email: this.email,
    role: this.role
  };
  
  return jwt.sign(payload, process.env.JWT_SECRET, {
    expiresIn: process.env.JWT_EXPIRES_IN || '24h',
    issuer: 'your-app-name',
    audience: 'your-app-users'
  });
};

// Advanced security middleware
const securityMiddleware = {
  // Input sanitization
  sanitizeInput: (req, res, next) => {
    const sanitizeValue = (value) => {
      if (typeof value === 'string') {
        return value.replace(/<script\b[^<]*(?:(?!<\/script>)<[^<]*)*<\/script>/gi, '');
      }
      if (typeof value === 'object' && value !== null) {
        Object.keys(value).forEach(key => {
          value[key] = sanitizeValue(value[key]);
        });
      }
      return value;
    };
    
    req.body = sanitizeValue(req.body);
    req.query = sanitizeValue(req.query);
    req.params = sanitizeValue(req.params);
    next();
  },

  // CSRF protection
  csrfProtection: (req, res, next) => {
    if (['POST', 'PUT', 'DELETE', 'PATCH'].includes(req.method)) {
      const token = req.headers['x-csrf-token'];
      if (!token || !validateCSRFToken(token, req.session.csrfSecret)) {
        return res.status(403).json({
          success: false,
          message: 'Invalid CSRF token'
        });
      }
    }
    next();
  },

  // SQL injection prevention for dynamic queries
  preventSQLInjection: (req, res, next) => {
    const checkForSQLInjection = (value) => {
      if (typeof value === 'string') {
        const sqlPatterns = [
          /(\b(SELECT|INSERT|UPDATE|DELETE|DROP|CREATE|ALTER|EXEC|UNION)\b)/i,
          /(--|\*\/|\/\*)/,
          /(\b(OR|AND)\s+\d+\s*=\s*\d+)/i
        ];
        
        return sqlPatterns.some(pattern => pattern.test(value));
      }
      return false;
    };
    
    const containsSQLInjection = [
      ...Object.values(req.body || {}),
      ...Object.values(req.query || {}),
      ...Object.values(req.params || {})
    ].some(checkForSQLInjection);
    
    if (containsSQLInjection) {
      return res.status(400).json({
        success: false,
        message: 'Potentially malicious input detected'
      });
    }
    
    next();
  }
};

// Advanced authentication with 2FA support
class AuthController {
  static async register(req, res) {
    try {
      const { name, email, password } = req.body;
      
      // Check if user already exists
      const existingUser = await User.findOne({ email });
      if (existingUser) {
        return res.status(400).json({
          success: false,
          message: 'User already exists with this email'
        });
      }
      
      // Create user
      const user = new User({ name, email, password });
      await user.save();
      
      // Generate email verification token
      const verificationToken = crypto.randomBytes(32).toString('hex');
      user.security.emailVerificationToken = verificationToken;
      await user.save();
      
      // Send verification email (implement email service)
      await EmailService.sendVerificationEmail(email, verificationToken);
      
      res.status(201).json({
        success: true,
        message: 'User registered successfully. Please check your email for verification.',
        data: {
          userId: user._id,
          email: user.email
        }
      });
      
    } catch (error) {
      console.error('Registration error:', error);
      res.status(500).json({
        success: false,
        message: 'Registration failed',
        error: process.env.NODE_ENV === 'development' ? error.message : 'Internal server error'
      });
    }
  }
  
  static async login(req, res) {
    try {
      const { email, password, twoFactorCode } = req.body;
      
      // Find user
      const user = await User.findOne({ email, isActive: true });
      if (!user) {
        return res.status(401).json({
          success: false,
          message: 'Invalid credentials'
        });
      }
      
      // Verify password
      await user.comparePassword(password);
      
      // Check 2FA if enabled
      if (user.security.twoFactorEnabled) {
        if (!twoFactorCode) {
          return res.status(200).json({
            success: true,
            requiresTwoFactor: true,
            message: 'Two-factor authentication code required'
          });
        }
        
        const verified = speakeasy.totp.verify({
          secret: user.security.twoFactorSecret,
          encoding: 'base32',
          token: twoFactorCode,
          window: 2
        });
        
        if (!verified) {
          return res.status(401).json({
            success: false,
            message: 'Invalid two-factor authentication code'
          });
        }
      }
      
      // Generate tokens
      const accessToken = user.generateAuthToken();
      const refreshToken = jwt.sign(
        { userId: user._id, type: 'refresh' },
        process.env.JWT_REFRESH_SECRET,
        { expiresIn: '7d' }
      );
      
      // Store refresh token in database
      await RefreshToken.create({
        token: refreshToken,
        userId: user._id,
        expiresAt: new Date(Date.now() + 7 * 24 * 60 * 60 * 1000)
      });
      
      res.json({
        success: true,
        message: 'Login successful',
        data: {
          user: user.toJSON(),
          accessToken,
          refreshToken
        }
      });
      
    } catch (error) {
      console.error('Login error:', error);
      res.status(401).json({
        success: false,
        message: error.message || 'Login failed'
      });
    }
  }
}
```

### **Part 4: Deployment & DevOps (10 minutes)**

#### **🚀 Production Deployment Pipeline**

```yaml
# .github/workflows/deploy.yml
name: Deploy Full-Stack Application

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  test:
    runs-on: ubuntu-latest
    
    services:
      mongodb:
        image: mongo:5.0
        ports:
          - 27017:27017
      redis:
        image: redis:6.2
        ports:
          - 6379:6379
    
    steps:
    - uses: actions/checkout@v3
    
    - name: Setup Node.js
      uses: actions/setup-node@v3
      with:
        node-version: '18'
        cache: 'npm'
    
    - name: Install dependencies
      run: |
        npm ci
        cd client && npm ci
    
    - name: Run linting
      run: |
        npm run lint
        cd client && npm run lint
    
    - name: Run backend tests
      run: npm run test:coverage
      env:
        NODE_ENV: test
        MONGODB_URI: mongodb://localhost:27017/test
        REDIS_URL: redis://localhost:6379
        JWT_SECRET: test-secret
    
    - name: Run frontend tests
      run: cd client && npm run test:coverage
    
    - name: Upload coverage reports
      uses: codecov/codecov-action@v3
      with:
        files: ./coverage/lcov.info,./client/coverage/lcov.info
    
    - name: Security audit
      run: |
        npm audit --audit-level moderate
        cd client && npm audit --audit-level moderate

  build:
    needs: test
    runs-on: ubuntu-latest
    if: github.ref == 'refs/heads/main'
    
    steps:
    - uses: actions/checkout@v3
    
    - name: Setup Node.js
      uses: actions/setup-node@v3
      with:
        node-version: '18'
        cache: 'npm'
    
    - name: Install dependencies
      run: |
        npm ci
        cd client && npm ci
    
    - name: Build frontend
      run: cd client && npm run build
      env:
        REACT_APP_API_URL: ${{ secrets.PRODUCTION_API_URL }}
        REACT_APP_ENVIRONMENT: production
    
    - name: Build Docker images
      run: |
        docker build -t myapp-backend .
        docker build -t myapp-frontend ./client
    
    - name: Configure AWS credentials
      uses: aws-actions/configure-aws-credentials@v2
      with:
        aws-access-key-id: ${{ secrets.AWS_ACCESS_KEY_ID }}
        aws-secret-access-key: ${{ secrets.AWS_SECRET_ACCESS_KEY }}
        aws-region: us-east-1
    
    - name: Login to Amazon ECR
      uses: aws-actions/amazon-ecr-login@v1
    
    - name: Push images to ECR
      run: |
        docker tag myapp-backend:latest ${{ secrets.ECR_REGISTRY }}/myapp-backend:latest
        docker tag myapp-frontend:latest ${{ secrets.ECR_REGISTRY }}/myapp-frontend:latest
        docker push ${{ secrets.ECR_REGISTRY }}/myapp-backend:latest
        docker push ${{ secrets.ECR_REGISTRY }}/myapp-frontend:latest

  deploy:
    needs: build
    runs-on: ubuntu-latest
    environment: production
    
    steps:
    - uses: actions/checkout@v3
    
    - name: Deploy to ECS
      run: |
        aws ecs update-service \
          --cluster production-cluster \
          --service myapp-backend-service \
          --force-new-deployment
        
        aws ecs update-service \
          --cluster production-cluster \
          --service myapp-frontend-service \
          --force-new-deployment
    
    - name: Wait for deployment
      run: |
        aws ecs wait services-stable \
          --cluster production-cluster \
          --services myapp-backend-service myapp-frontend-service
    
    - name: Run health checks
      run: |
        curl -f ${{ secrets.PRODUCTION_API_URL }}/health || exit 1
        curl -f ${{ secrets.PRODUCTION_FRONTEND_URL }} || exit 1
    
    - name: Notify deployment
      uses: 8398a7/action-slack@v3
      with:
        status: ${{ job.status }}
        channel: '#deployments'
        webhook_url: ${{ secrets.SLACK_WEBHOOK }}
      if: always()
```

```dockerfile
# Production Dockerfile for backend
FROM node:18-alpine AS builder

WORKDIR /app
COPY package*.json ./
RUN npm ci --only=production && npm cache clean --force

FROM node:18-alpine AS runtime

# Security: Create non-root user
RUN addgroup -g 1001 -S nodejs
RUN adduser -S nodeuser -u 1001

WORKDIR /app

# Copy production dependencies
COPY --from=builder --chown=nodeuser:nodejs /app/node_modules ./node_modules
COPY --chown=nodeuser:nodejs . .

# Security: Remove unnecessary packages
RUN apk del --purge apk-tools

# Health check
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
  CMD curl -f http://localhost:3000/api/health || exit 1

USER nodeuser

EXPOSE 3000

CMD ["node", "server.js"]
```

---

## 🛠️ **Hands-On Project: E-commerce Platform**

Build a complete e-commerce platform with React frontend, Node.js backend, and MongoDB database.

### **Project Requirements**

1. ✅ User authentication with JWT and 2FA
2. ✅ Product catalog with search and filtering
3. ✅ Shopping cart and checkout process
4. ✅ Payment integration (Stripe)
5. ✅ Order management and tracking
6. ✅ Admin dashboard for inventory management
7. ✅ Real-time notifications with WebSocket
8. ✅ Automated testing and CI/CD deployment

**Expected Outcome**: Production-ready e-commerce platform deployed to AWS with monitoring and analytics.

---

## 🎯 **Next Steps & Advanced Topics**

### **Advanced Learning Path**

1. **Microservices Architecture** - Breaking monoliths into scalable services
2. **GraphQL APIs** - Modern API development with efficient data fetching
3. **Real-time Applications** - WebSocket implementation and scaling
4. **Performance Optimization** - Advanced caching, CDN, and database optimization
5. **Cloud-Native Development** - Kubernetes, serverless, and container orchestration

### **Career Progression**

- **Full-Stack Developer**: $90K - $140K
- **Senior Full-Stack Developer**: $120K - $180K  
- **Technical Lead**: $150K - $220K
- **Engineering Manager**: $180K - $300K

---

## ✅ **Lesson Complete!**

**🎉 Congratulations!** You've mastered advanced web development with React and Node.js, including professional architecture patterns, security implementation, and production deployment strategies.

**🚀 Ready for Next Lesson**: [Microservices Architecture](../advanced/microservices-architecture.md)

---

*This lesson is part of the **Learn-Library Professional Technology Education Platform**.*
