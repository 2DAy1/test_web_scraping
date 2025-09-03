# XPath Expressions for marketdino.pl

## Location Information

### Primary Pattern
```xpath
//p[contains(text(), 'gmina') or contains(text(), 'opolskie') or contains(text(), 'kujawsko-pomorskie') or contains(text(), 'wielkopolskie')]
```

### Alternative Patterns
```xpath
//p[contains(@class, 'location') or contains(@class, 'address')]
//p[contains(text(), ',') and contains(text(), 'skie')]
```

### Specific Patterns
```xpath
//p[contains(text(), '47-143') or contains(text(), '87-840') or contains(text(), '63-700')]
//p[contains(text(), 'Przemysłowa') or contains(text(), 'Kaliska') or contains(text(), 'Krotoszyn')]
```

## Email Detection

### Primary Pattern
```xpath
//*[contains(text(), '@') and contains(text(), '.')]
```

### Alternative Patterns
```xpath
//*[matches(text(), '[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}')]
//a[contains(@href, 'mailto:')]
```

## Notes

- Primary patterns are most practical due to simplicity and reliability
- Specific patterns are very accurate but less universal
- Use primary patterns for general location and email detection

