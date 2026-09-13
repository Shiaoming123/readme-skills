#!/usr/bin/env node

const args = process.argv.slice(2);
const inputIndex = args.indexOf("--input");

if (args.includes("--help") || inputIndex === -1 || !args[inputIndex + 1]) {
  console.log("Usage: clipulse --input <file>");
  process.exit(args.includes("--help") ? 0 : 1);
}

console.log(`Queued ${args[inputIndex + 1]}`);
