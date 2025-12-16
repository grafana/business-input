// Jest setup provided by Grafana scaffolding
import './.config/jest-setup';

// Polyfill for Web Streams API (used by @grafana/llm dependencies)
import { TransformStream, ReadableStream, WritableStream } from 'stream/web';
Object.assign(global, { TransformStream, ReadableStream, WritableStream });
