---
tags:
  - Business Input
title: 'Business Input'
description: 'Learn how to store and emulate data in Grafana using the Business Input data source plugin.'
labels:
  products:
    - enterprise
    - oss
weight: 10
---

# Business Input

The Business Input data source is a plugin for Grafana that allows storing and emulating your data.

## Requirements

- Business Input data source version 5.X requires **Grafana 11** or **Grafana 12**.
- Business Input data source version 4.X requires **Grafana 10.2** or **Grafana 11**.
- Static data source version 3.X requires **Grafana 9.2** or **Grafana 10**.
- Static data source version 2.X requires **Grafana 8.5** or **Grafana 9**.
- Static data source version 1.X requires **Grafana 7.3**.

## Getting started

The Business Input data source can be installed from the [Grafana Catalog](https://grafana.com/grafana/plugins/marcusolsson-static-datasource/) or utilizing the Grafana command line tool.

<Youtube
  id="1qYzHfPXJF8"
  title="Install Business Suite plugins in Cloud, OSS, Enterprise. Getting started with the Business Suite."
/>

For the latter, please use the following command.

```sh
grafana cli plugins install marcusolsson-static-datasource
```

## Highlights

- Create static visualizations that don't depend on a specific data source.
- Allows specifying values [manually or using the **JavaScript Values Editor**](/plugins/business-input/panels/business-charts/) code.
- Allows to generate data with OpenAI and LLM App.
- Build custom query responses for testing or developing panel plugins.
- Store data and images directly in the dashboard.
- Supports variables in the text fields.
- Uses Number input for Number, Date Time Picker for Time fields.
- Uses Text Area for String inputs with more than 100 symbols.

<Image
  title="Display Pie Charts based on the data from the Static Data Source."
  src="/img/plugins/business-input/dashboard.png"
/>

## Tutorial

In this 6-minute tutorial, Daria explains what the plugin does. She demonstrates how to work with its parameters and use it for visualization panel discovery, data storage, and troubleshooting.

Daria still references the plugin using its old name. The newer version of the plugin review video is in the works and will be published as soon as it is available.

<Youtube
  id="QOV8ECOUjWs"
  title="Mimic any data with the Business Input data source."
/>


## Documentation

| Section                      | Description                                                  |
| ---------------------------- | ------------------------------------------------------------ |
| [Provisioning](provisioning) | Demonstrates how to automatically provision the Data Source. |
| [Variables](variables)       | Demonstrates how to use variables.                           |
| [Panels](panels)             | Demonstrates how to use data source with panels.             |
| [Release Notes](release)     | Stay up to date with the latest features and updates.        |

## License

Apache License Version 2.0, see [LICENSE](https://github.com/volkovlabs/business-input/blob/main/LICENSE).

