# Regular Expressions

## Patterns

### 1. URL Pattern
```
https?://[^\s<>"{}|\\^`\[\]]+
```

### 2. Email Pattern
```
\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b
```

### 3. Telegram/Viber Bot Pattern
```
@[A-Za-z0-9_]+
```

### 4. Parentheses Text Pattern
```
\([^)]+\)
```

## Testing

Use https://regex101.com/ to test these patterns.

## Results

- **URL**: 5 found
- **Email**: 1 found
- **Bots**: 3 found
- **Parentheses text**: 1 found

