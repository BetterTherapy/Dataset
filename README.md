# Mental Health Dataset Generator

A Python application that generates mental health Q&A datasets using Hugging Face language models and stores them in a PostgreSQL database. This project is designed to create training data for mental health AI assistants by generating compassionate questions and empathetic responses.

## 🚀 Features

- **AI-Powered Generation**: Uses Meta's Llama-3.1-8B-Instruct model to generate mental health questions and responses
- **Database Storage**: PostgreSQL integration with SQLAlchemy ORM for data persistence
- **Configurable Generation**: Adjustable parameters for model settings and data generation count
- **Database Migrations**: Alembic integration for database schema management
- **Rich Logging**: Beautiful console output with structured logging

## 📋 Prerequisites

- Python 3.12 or higher
- PostgreSQL database
- Sufficient RAM (20GB+ recommended for model loading)
- GPU with CUDA support (optional, can run on CPU)

## 🛠️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/BetterTherapy/Dataset.git
cd Dataset
```

### 2. Install Dependencies

This project uses `uv` for dependency management. Install it first if you don't have it:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Then install the project dependencies:

```bash
uv sync
```

Alternatively, you can use pip:

```bash
pip install -e .
```

### 3. Environment Setup

Copy `.env.example` to `.env` file in the project root and update following variables:

```bash
cp .env.example .env
```

```bash
# Database Configuration
DATABASE_URL=postgresql://username:password@localhost:5432/database_name

# Model Configuration (optional - defaults provided)
MODEL_NAME=meta-llama/Llama-3.1-8B-Instruct
OFFLOAD_TO_CPU=true
VRAM_IN_GIB=16
CPU_IN_GIB=20

# Generation Configuration
DATA_COUNT=1000
```

**Important**: Replace the database URL with your actual PostgreSQL connection string.

## 🗄️ Database Setup

### 1. Create PostgreSQL Database

```bash
create database mental_health_dataset
```

### 2. Run Database Migrations

Initialize Alembic and run migrations:

```bash
# Initialize the database schema
alembic upgrade head
```

## 🚀 Usage

### Basic Usage

Run the main application to generate mental health Q&A pairs:

```bash
python main.py
```

### Configuration Options

You can customize the generation process by modifying the `.env` file or setting environment variables:

- **`MODEL_NAME`**: Hugging Face model identifier (default: `meta-llama/Llama-3.1-8B-Instruct`)
- **`DATA_COUNT`**: Number of Q&A pairs to generate (default: 1000)
- **`OFFLOAD_TO_CPU`**: Whether to run the model on CPU (default: true)
- **`VRAM_IN_GIB`**: GPU VRAM requirement in GB (default: 16)
- **`CPU_IN_GIB`**: CPU RAM requirement in GB (default: 20)

## 📁 Project Structure

```
dataset/
├── alembic/                 # Database migration files
├── database/               # Database models and connection
│   ├── model.py           # SQLAlchemy models
│   ├── connection.py      # Database connection setup
│   ├── query.py           # Database query functions
│   └── session.py         # Session management
├── hf_model/              # Hugging Face model integration
│   ├── generator.py       # Response generation logic
│   └── init_model.py      # Model initialization
├── config.py              # Configuration management
├── main.py                # Main application entry point
├── pyproject.toml         # Project dependencies and metadata
└── README.md              # This file
```

## 🔧 Development

### Code Formatting

```bash
uv run ruff check --fix .
```

## 📊 Generated Data Format

The application generates data in the following format:

- **Table**: `base_prompt_response`
- **Columns**:
  - `id`: Primary key
  - `prompt`: Mental health question
  - `response`: Empathetic answer
  - `is_used`: Boolean flag for tracking usage

## 🚨 Important Notes

1. **Model Size**: The default Llama-3.1-8B-Instruct model requires significant RAM. Ensure your system meets the memory requirements.
2. **Database**: Make sure PostgreSQL is running and accessible before starting the application.
3. **Environment Variables**: The `.env` file is required for database connection and model configuration.
4. **Model Licensing**: Ensure you comply with the license terms of any Hugging Face model you use.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📄 License

This project is licensed under the terms of the [MIT License](LICENSE).

## 🆘 Troubleshooting

### Common Issues

1. **Database Connection Error**: Verify your PostgreSQL connection string and ensure the database is running
2. **Memory Issues**: Reduce `DATA_COUNT` or enable `OFFLOAD_TO_CPU` for lower memory usage
3. **Model Download Issues**: Check your internet connection and Hugging Face access permissions

### Getting Help

If you encounter issues:

1. Check the logs for error messages
2. Verify your environment configuration
3. Ensure all dependencies are properly installed
4. Check that your system meets the memory requirements
