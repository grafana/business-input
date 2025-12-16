---
title: JavaScript Values Editor
description: Learn how to use the JavaScript Values Editor to generate data frames and import external libraries.
keywords:
  - business input
labels:
  products:
    - cloud
    - enterprise
    - oss
---

# JavaScript Values Editor

{{< admonition type="note" >}}
The JavaScript Values Editor must return a data frame.
{{< /admonition >}}

```js
const result = {
  ...frame,
  fields: frame.fields.map((field) => ({
    ...field,
    values: [],
  })),
};

return Promise.resolve(result);
```

{{< figure src="/media/docs/grafana/panels-visualizations/business-input/import-js.png" class="border" alt="Enable JavaScript Values Editor to get access to JavaScript area." >}}

## Imports

The Business Input data source supports importing libraries in the **JavaScript** editor mode.
You can import external or local libraries.

```js
import("https://esm.sh/mermaid").then(({ default: mermaid }) => {
  mermaid.initialize({ startOnLoad: true });

  mermaid.run({
    querySelector: ".mermaid",
    suppressErrors: false,
  });
});

const array = Array.from({ length: 3 }, (v, i) => `${i + 1}`);

const result = {
  ...frame,
  fields: frame.fields.map((field) => {
    return {
      ...field,
      values: array.map((item) => {
        return item;
      }),
    };
  }),
};

return Promise.resolve(result);
```
