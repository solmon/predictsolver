import { Injectable } from '@nestjs/common';

@Injectable()
export class AppService {
  getHello(): object {
    return {
      name: 'PredictSolver Data API',
      description: 'RESTful API for accessing PredictSolver ML models',
      version: '1.0.0',
      endpoints: {
        '/': 'API information (this response)',
        '/models': 'Get available ML models',
        '/models/:modelId/predict': 'Make predictions using a specific model'
      }
    };
  }
}
