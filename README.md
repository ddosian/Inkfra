![Logo](/imgs/logo/mocha-no-bg.svg)

[![Release](https://img.shields.io/github/v/release/ddosian/inkfra)](https://github.com/ddosian/Inkfra/releases/latest)
[![Docker Hub](https://img.shields.io/docker/pulls/ddosian/inkfra)](https://hub.docker.com/r/ddosian/inkfra)
[![Workflow Status](https://img.shields.io/github/actions/workflow/status/ddosian/inkfra/docker.yaml)](https://github.com/ddosian/inkfra/actions)

Static site generator for network diagrams and documentation.

## Features

- **YAML-Based Configuration** — Define your diagrams declaratively
- **Multiple Themes** — Built-in dark and light themes
- **Category Styling** — Color-code your components by category with customizable colors
- **Docker Ready** — Fully containerized for easy deployment
- **Flexible** — Add titles, descriptions, tags, and categories to organize your infrastructure

## Quick Start

### Docker Compose (recommended)

Copy `compose.example.yaml` and run the following:

```bash
# Start the container
docker compose up -d
```

### Using Docker

```bash
docker run -d \
  -v $(pwd)/config:/config \
  -v $(pwd)/output:/output \
  -e THEME=catppuccin-mocha \
  ddosian/inkfra
```

### Local Setup

1. **Prerequisites**: Python 3.8+
2. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

3. **Create your configuration** — See the [Configuration](#configuration) section below

4. **Run the generator**:
   ```bash
   python src/main.py
   ```

## Configuration

Create a YAML file in your config directory to define your diagram. Here's an example:

```yaml
title: "My Infrastructure"
theme: "catppuccin-mocha"
tags: ["Networking", "Production"]

content:
  wan:
    name: "Internet"
    github:
      icon: "mdi:github"
      title: "GitHub"
      description: "Version Control"
      category: "external"

  compute:
    name: "Servers"
    server-01:
      icon: "mdi:server"
      title: "Web Server"
      description: "Primary web application"
      category: "production"
    database-01:
      icon: "mdi:database"
      title: "Database"
      description: "PostgreSQL instance"
      category: "production"

categories:
  external:
    color: yellow
  production:
    color: red
```

### Configuration Reference

| Field        | Type   | Description                                               |
| ------------ | ------ | --------------------------------------------------------- |
| `title`      | string | Title of your diagram                                     |
| `theme`      | string | Theme name (e.g., `catppuccin-mocha`, `catppuccin-latte`) |
| `tags`       | array  | Array of tags for categorization                          |
| `content`    | object | Sections and components of your diagram                   |
| `categories` | object | Category definitions with color values                    |

### Icons

Icons are specified using [Material Design Icons](https://materialdesignicons.com/) format: `mdi:icon-name`

## Environment Variables

Control Inkfra's behavior with environment variables:

| Variable         | Default    | Description                                       |
| ---------------- | ---------- | ------------------------------------------------- |
| `CONFIG_DIR`     | `/config/` | Directory containing YAML configuration files     |
| `OUTPUT_DIR`     | `/output/` | Directory where HTML output is generated          |
| `CHECK_INTERVAL` | `10`       | Interval (in seconds) to check for config changes |
| `DEBUG_OUTPUT`   | `False`    | Enable debug logging                              |

### Example with Environment Variables

```bash
docker run -d \
  -v $(pwd)/config:/config \
  -v $(pwd)/output:/output \
  -e CONFIG_DIR=/config/ \
  -e OUTPUT_DIR=/output/ \
  -e THEME=catppuccin-latte \
  -e CHECK_INTERVAL=5 \
  -e DEBUG_OUTPUT=false \
  ddosian/inkfra
```

## Themes

Inkfra includes two Catppuccin color scheme variants:

- **catppuccin-mocha** — Dark theme
- **catppuccin-latte** — Light theme

Themes can be customized by modifying the CSS files in the `themes/` directory.

## License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests to improve Inkfra.

## Support

For issues, feature requests, or questions, please open an issue on the [GitHub repository](https://github.com/ddosian/Inkfra/issues).
