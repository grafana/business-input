---
title: LLM App and OpenAI
description: Learn how to generate data using LLM models and OpenAI integration with the Business Input data source.
keywords:
  - business input
  - llm
labels:
  products:
    - cloud
    - enterprise
    - oss
---

# LLM App and OpenAI

The Business Input Data Source supports LLM models (OpenAI, custom) using LLM App from Grafana.

## LLM App

Add [LLM App](https://grafana.com/grafana/plugins/grafana-llm-app/) plugin and set up `OpenAI API Key` with `OpenAI API Organization ID`.

{{< figure src="/media/docs/grafana/panels-visualizations/business-input/llm-app.png" class="border" alt="Configure LLM App plugin for Grafana to set API key and organization ID." >}}

When LLM App configured, a text area will appear in `Code` editor mode of the Business Input Data Source.

{{< admonition type="note" >}}
Dashboard and Global variable are supported in the text area.
{{< /admonition >}}

This text area allows you to use the response that will be received from the LLM App together with OpenAI. The result is stored in `context.llmResult`.

{{< figure src="/media/docs/grafana/panels-visualizations/business-input/llm-app-message-box.png" class="border" alt="Result returned from LLM App for BTC price." >}}

## Example with BTC price

### Message

```js
Please return JSON with 2 arrays: datetime and price which contain BTC price
from ${__from:date} to ${__to:date} for every hour
```

### JavaScript code editor

```js
console.log("result", context.llmResult);

const content = context.llmResult?.choices?.[0]?.message?.content;
let data = {};

try {
  data = JSON.parse(content);
} catch (e) {
  console.error("Unable to parse result", e);
}

console.log("parsedData", data);

const result = {
  ...frame,
  fields: frame.fields.map((field) => ({
    ...field,
    values: field.name === "date" ? data.datetime || [] : data.price || [],
  })),
};

return Promise.resolve(result);
```

### Result

Produced data frame with results can be displayed with any panel plugin.

{{< figure src="/media/docs/grafana/panels-visualizations/business-input/llm-result.png" class="border" alt="Display OpenAI results for BTC price using native Time Series panel." >}}
