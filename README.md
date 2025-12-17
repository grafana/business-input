# Business Input for Grafana

[![Grafana](https://img.shields.io/badge/Grafana-12.0-orange)](https://grafana.com/)

This project was originally contributed by [Volkov Labs](https://github.com/volkovlabs/business-text) - thanks for all your great work!

> [!CAUTION]
> This data source plugin is now in maintenance mode. It will continue to receive only minimal updates required for compatibility with Grafana 12.x.
> No new features will be developed. To ensure long-term support and access to new capabilities, we recommend using the [Infinity data source plugin](https://grafana.com/grafana/plugins/yesoreyeram-infinity-datasource/).  

## Legacy information

**Business Input** is a powerful Grafana plugin that enables you to store, emulate, and visualize static data effortlessly. Perfect for testing, prototyping, or creating custom visualizations without relying on external data sources.

[![Business Input Data Source for Grafana | Mimic Any Data Source | Tutorial & Examples](https://raw.githubusercontent.com/volkovlabs/business-input/main/img/video.png)](https://youtu.be/QOV8ECOUjWs)

## 🚀 Features

- **Static Visualizations**: Create dashboards independent of specific data sources.
- **Flexible Data Input**: Manually enter values or use the JavaScript Values Editor for dynamic data.
- **AI-Powered Data Generation**: Generate data using OpenAI and LLM applications.
- **Custom Query Responses**: Build tailored responses for testing or developing panel plugins.
- **Dashboard Storage**: Store data and images directly within Grafana dashboards.
- **Variable Support**: Use variables in text fields for dynamic content.
- **Intuitive Inputs**: Leverage Number inputs, Date Time Pickers, and Text Areas for seamless data entry.

## 📋 Requirements

Ensure your Grafana version matches the plugin version for compatibility:

| Plugin Version | Compatible Grafana Versions |
| -------------- | --------------------------- |
| 5.X            | Grafana 11, Grafana 12      |
| 4.X            | Grafana 10.3, Grafana 11    |
| 3.X            | Grafana 9.2, Grafana 10     |
| 2.X            | Grafana 8.5, Grafana 9      |
| 1.X            | Grafana 7.3                 |

## 🛠️ Installation

Install the Business Input data source via the [Grafana Plugins Catalog](https://grafana.com/grafana/plugins/marcusolsson-static-datasource/) or using the Grafana CLI:

```bash
grafana cli plugins install marcusolsson-static-datasource
```

[![Install Business Suite Plugins in Cloud, OSS, Enterprise | Open Source Community Plugins](https://raw.githubusercontent.com/volkovlabs/.github/main/started.png)](https://youtu.be/1qYzHfPXJF8)

## 📚 Documentation

Explore detailed guides and tutorials to maximize the potential of Business Input:

| Section  | Description                                           |
| -------- | ----------------------------------------------------- |
| [Provisioning](https://grafana.com/docs/plugins/marcusolsson-static-datasource/latest/provisioning/) | Learn how to automatically provision the data source. |
| [Variables](https://grafana.com/docs/plugins/marcusolsson-static-datasource/latest/variables/)       | Understand how to use variables for dynamic data.     |
| [Panels](https://grafana.com/docs/plugins/marcusolsson-static-datasource/latest/panels/)             | See how to integrate with Grafana panels.             |
| [Release Notes](https://grafana.com/docs/plugins/marcusolsson-static-datasource/latest/release/)     | Stay updated with the latest features and changes.    |

## 🌟 Business Suite for Grafana

Business Input is part of the **Business Suite**, a collection of open-source plugins by Volkov Labs designed to solve common business challenges with intuitive interfaces, comprehensive documentation, and video tutorials.

[![Business Suite for Grafana](https://raw.githubusercontent.com/VolkovLabs/.github/main/business.png)](https://volkovlabs.io/plugins/)

## 📜 License

This project is licensed under the Apache License Version 2.0. See the [LICENSE](https://github.com/grafana/business-input/blob/main/LICENSE) file for details.
