# HyWrapper - TypeScript Hypixel API Wrapper

A TypeScript wrapper for the Hypixel API.

## Installation

```bash
npm install hywrapper-ts
```

## Usage

```typescript
import { HypixelClient } from 'hywrapper-ts';

async function main() {
    const client = new HypixelClient('your-api-key');
    const response = await client.getPlayer('ac29411d0826412f98c0dd14b334c1fa');
    
    if (response.success) {
        console.log(`Player Found: ${response.player?.displayname}`);
    }
}

main();
```

## Features

- Strong TypeScript definitions
- Promise-based API
- Supports all major Hypixel API endpoints

## Building

To build the project manually:

```bash
npm install
npm run build
```
