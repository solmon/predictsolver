import { ApiProperty } from '@nestjs/swagger';

export class ModelInfoDto {
  @ApiProperty({
    description: 'List of available models',
    type: 'array'
  })
  models: ModelDto[];

  @ApiProperty({
    description: 'API version',
    example: '0.1.0'
  })
  version: string;
}

export class ModelDto {
  @ApiProperty({
    description: 'Model identifier',
    example: 'linear_regression'
  })
  id: string;

  @ApiProperty({
    description: 'Display name of the model',
    example: 'Linear Regression'
  })
  name: string;

  @ApiProperty({
    description: 'Type of the model (regression, classification, etc)',
    example: 'regression'
  })
  type: string;

  @ApiProperty({
    description: 'Short description of the model',
    example: 'Standard linear regression model'
  })
  description: string;
}
