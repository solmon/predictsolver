import { Controller, Get, Post, Body, Param } from '@nestjs/common';
import { ApiTags, ApiOperation, ApiResponse, ApiParam } from '@nestjs/swagger';
import { ModelsService } from './models.service';
import { PredictionRequestDto, PredictionResponseDto } from './dto/prediction.dto';
import { ModelInfoDto } from './dto/model-info.dto';

@ApiTags('models')
@Controller('models')
export class ModelsController {
  constructor(private readonly modelsService: ModelsService) {}

  @Get()
  @ApiOperation({ summary: 'Get available models' })
  @ApiResponse({
    status: 200,
    description: 'List of available ML models',
    type: ModelInfoDto
  })
  async getModelInfo(): Promise<ModelInfoDto> {
    return this.modelsService.getModelInfo();
  }

  @Post(':modelId/predict')
  @ApiOperation({ summary: 'Make a prediction with a specific model' })
  @ApiParam({
    name: 'modelId',
    description: 'ID of the model to use for prediction',
    example: 'linear_regression'
  })
  @ApiResponse({
    status: 200,
    description: 'Prediction result',
    type: PredictionResponseDto
  })
  @ApiResponse({
    status: 400,
    description: 'Bad request or model not found',
    type: PredictionResponseDto
  })
  async predict(
    @Param('modelId') modelId: string,
    @Body() predictionRequest: PredictionRequestDto
  ): Promise<PredictionResponseDto> {
    return this.modelsService.predict(modelId, predictionRequest.data);
  }
}
