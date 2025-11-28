---
title: Business Charts
description: Learn how to create data for the Business Charts panel using manual values or the JavaScript Values Editor.
keywords:
  - business input
labels:
  products:
    - cloud
    - enterprise
    - oss
---

# Business Charts

You can use the Business Input data source to test the [Business Charts panel](https://grafana.com/docs/plugins/volkovlabs-echarts-panel/<PLUGINS_VERSION>/). The following examples show how to create values:

- Manually
- By using the **JavaScript Values Editor**

Both examples use the Business Charts [Visual Editor](https://grafana.com/docs/plugins/volkovlabs-echarts-panel/<PLUGINS_VERSION>/visualeditor/) to read the data frame values and pass them to the Business Charts.

{{< admonition type="note" >}}
You can use the Business Charts demo project to play with both the Business Input data source settings and the Business Charts parameters following the link [Business Charts Pie examples](https://echarts.volkovlabs.io/d/0b5-q7K4k/pie?orgId=1). Go to Edit mode and start experimenting.
{{< /admonition >}}

## Manual

You can use the Business Input data source to add files and values manually.

{{< figure src="/media/docs/grafana/panels-visualizations/business-input/bi-charts-pie-manual-editor.png" class="border" alt="The Business Charts Pie Chart using Manual mode." >}}

## JavaScript Values Editor

You can use the JavaScript **Values Editor** to generate data frame values.

{{< figure src="/media/docs/grafana/panels-visualizations/business-input/bi-charts-pie-code-editor.png" class="border" alt="The Business Charts Pie Chart using JavaScript Code mode." >}}

The following JavaScript code creates values for the Business Input data source:

```javascript
const values = [
  ["Search Engine", "Direct", "Email", "Union Ads", "Video Ads"],
  [1048, 735, 580, 484, 300],
];

const result = {
  ...frame,
  fields: frame.fields.map((field, index) => ({
    ...field,
    values: values[index],
  })),
};

return Promise.resolve(result);
```

The Business Charts function.

```javascript
return {
  dataset: {
    source: context.editor.dataset.source,
  },
  tooltip: {
    trigger: "item",
  },
  series: [
    {
      name: "Access From",
      type: "pie",
      radius: "80%",
      emphasis: {
        itemStyle: {
          shadowBlur: 10,
          shadowOffsetX: 0,
          shadowColor: "rgba(0, 0, 0, 0.5)",
        },
      },
    },
  ],
};
```
