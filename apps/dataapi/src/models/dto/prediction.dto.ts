import { IsString, IsOptional, IsObject, ValidateNested } from 'class-validator';
import { ApiProperty } from '@nestjs/swagger';
import { Type } from 'class-transformer';

export class PredictionRequestDto {
  @ApiProperty({
    description: 'Input data for prediction',
    example: { x: 5 }, 
    required: true
  })
  @IsObject()
  readonly data: Record<string, any>;
}

export class PredictionResponseDto {
  @ApiProperty({
    description: 'Prediction result',
    example: 22.5
  })
  prediction: number | string;

  @ApiProperty({
    description: 'ID of the model used for prediction',
    example: 'linear_regression'
  })
  modelId: string;

  @ApiProperty({
    description: 'Class name (for classification models)',
    example: 'high',
    required: false
  })
  @IsOptional()
  @IsString()
  className?: string;

  @ApiProperty({
    description: 'Error message if prediction failed',
    required: false
  })
  @IsOptional()
  @IsString()
  error?: string;

  @ApiProperty({
    description: 'Additional details',
    required: false
  })
  @IsOptional()
  details?: any;
}
