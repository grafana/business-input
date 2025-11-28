---
title: Variables
description: Learn how to use dashboard and global variables in the Business Input data source string fields.
keywords:
  - business input
  - variables
labels:
  products:
    - cloud
    - enterprise
    - oss
weight: 30
---

# Variables

The Business Input Data Source supports dashboard and global variables in the String fields.

Three types of variables are discussed in the [Grafana Crash Course](/grafana/variables).

## Code Editor

Create new `custom` variable:

```js
2022-02-10T00:00:00.000Z,
2022-03-10T00:00:00.000Z,
2022-04-10T00:00:00.000Z
```

{{< figure src="/media/docs/grafana/panels-visualizations/business-input/1st-variable.png" class="border" alt="Variable `from`" >}}

- Create another variable related to the first variable using the `Business Input Data Source` and `Code editor` variable type `Query`. Query options -> Data source -> `Static`.
- Take the value of the `from` variable and add 7 days to it for each iteration.
- Use `${variable_name}` syntax to use your variable in code.

### Code

```js
const array = Array.from({ length: 3 }, (v, i) => `${i + 1}`);

const result = {
  ...frame,
  fields: frame.fields.map((field) => ({
    ...field,
    values: array.map((item) => {
      const currentFrom = `${from}`;
      const date = new Date(currentFrom);
      const newTo = new Date(date.getTime() + item * 7 * 24 * 60 * 60 * 1000);
      return newTo.toISOString();
    }),
  })),
};

return Promise.resolve(result);
```

{{< figure src="/media/docs/grafana/panels-visualizations/business-input/2nd-variable.png" class="border" alt="Fill values for variable." >}}

Values for `to` variable will be:

```js
2022-02-17T00:00:00.000Z
2022-02-24T00:00:00.000Z
2022-03-03T00:00:00.000Z
```

Now every change value for variable `from` change values and for variable `to`:

{{< figure src="/media/docs/grafana/panels-visualizations/business-input/variable-reference.png" class="border" alt="Change of From variable will update variable To." >}}

{{< figure src="/media/docs/grafana/panels-visualizations/business-input/variable-reference-2.png" class="border" alt="Change of From variable will update variable To." >}}

## Manual Editor

Variable can be used in `Manual editor`. Use `$variable_name` syntax in input field.

{{< figure src="/media/docs/grafana/panels-visualizations/business-input/manual-editor-variable.png" class="border" alt="Variable in Manual Editor." >}}
