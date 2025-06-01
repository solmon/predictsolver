# PredictSolver Data API

This is a NestJS-based RESTful API for the PredictSolver platform. It provides access to machine learning models implemented in the Python core library.

<p align="center">
  <img src="https://nestjs.com/img/logo-small.svg" width="120" alt="Nest Logo" />
</p>

## Description

The Data API serves as a bridge between client applications and the PredictSolver machine learning models. It provides:

- RESTful endpoints for model discovery
- Prediction services for various ML models
- Swagger documentation
- Integration with the Python core library

## API Endpoints

- `GET /api` - API information
- `GET /api/models` - List all available ML models
- `POST /api/models/:modelId/predict` - Make a prediction using a specific model
- `GET /api/docs` - Swagger API documentation

## Project Setup

There are two ways to set up and run the Data API:

### 1. Using the Monorepo Poethepoet Tasks

From the root of the monorepo:

```bash
# Install all dependencies including NestJS
$ poe install-dataapi

# Run the API in development mode
$ poe run-dataapi-dev

# Run the API in production mode
$ poe run-dataapi
```

### 2. Direct NestJS Commands

From this directory:

```bash
# Install dependencies
$ pnpm install

# Development mode with hot reload
$ pnpm run start:dev

# Production mode
$ pnpm run start:prod
```

## API Documentation

The API documentation is available at `/api/docs` when the server is running. This is powered by Swagger.

## Integration with Python Core

This API integrates with the Python core library through a special service that spawns Python processes to execute predictions and retrieve model information. This integration allows for seamless usage of advanced machine learning models built in Python.

## Testing

```bash
# Unit tests
$ pnpm run test

# e2e tests
$ pnpm run test:e2e

# Integration test (from monorepo root)
$ poe integration-test
```

# e2e tests
$ pnpm run test:e2e

# test coverage
$ pnpm run test:cov
```

## Deployment

When you're ready to deploy your NestJS application to production, there are some key steps you can take to ensure it runs as efficiently as possible. Check out the [deployment documentation](https://docs.nestjs.com/deployment) for more information.

If you are looking for a cloud-based platform to deploy your NestJS application, check out [Mau](https://mau.nestjs.com), our official platform for deploying NestJS applications on AWS. Mau makes deployment straightforward and fast, requiring just a few simple steps:

```bash
$ pnpm install -g mau
$ mau deploy
```

With Mau, you can deploy your application in just a few clicks, allowing you to focus on building features rather than managing infrastructure.

## Resources

Check out a few resources that may come in handy when working with NestJS:

- Visit the [NestJS Documentation](https://docs.nestjs.com) to learn more about the framework.
- For questions and support, please visit our [Discord channel](https://discord.gg/G7Qnnhy).
- To dive deeper and get more hands-on experience, check out our official video [courses](https://courses.nestjs.com/).
- Deploy your application to AWS with the help of [NestJS Mau](https://mau.nestjs.com) in just a few clicks.
- Visualize your application graph and interact with the NestJS application in real-time using [NestJS Devtools](https://devtools.nestjs.com).
- Need help with your project (part-time to full-time)? Check out our official [enterprise support](https://enterprise.nestjs.com).
- To stay in the loop and get updates, follow us on [X](https://x.com/nestframework) and [LinkedIn](https://linkedin.com/company/nestjs).
- Looking for a job, or have a job to offer? Check out our official [Jobs board](https://jobs.nestjs.com).

## Support

Nest is an MIT-licensed open source project. It can grow thanks to the sponsors and support by the amazing backers. If you'd like to join them, please [read more here](https://docs.nestjs.com/support).

## Stay in touch

- Author - [Kamil Myśliwiec](https://twitter.com/kammysliwiec)
- Website - [https://nestjs.com](https://nestjs.com/)
- Twitter - [@nestframework](https://twitter.com/nestframework)

## License

Nest is [MIT licensed](https://github.com/nestjs/nest/blob/master/LICENSE).
