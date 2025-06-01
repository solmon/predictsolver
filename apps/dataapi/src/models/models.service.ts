import { Injectable, Logger } from '@nestjs/common';
import { spawn } from 'child_process';
import * as fs from 'fs';
import * as path from 'path';
import * as os from 'os';

@Injectable()
export class ModelsService {
  private readonly logger = new Logger(ModelsService.name);
  private readonly pythonExecutable = 'python';
  private readonly tempDir = os.tmpdir();

  async getModelInfo() {
    const scriptPath = this.createPythonScript(`
import sys
import json
from predictsolver_core.api import get_model_info

result = get_model_info()
print(json.dumps(result))
`);

    try {
      const result = await this.runPythonScript(scriptPath);
      return JSON.parse(result);
    } catch (error) {
      this.logger.error(`Error getting model info: ${error.message}`);
      return { error: 'Failed to get model information', details: error.message };
    } finally {
      this.cleanupTempFile(scriptPath);
    }
  }

  async predict(modelId: string, data: any) {
    const scriptPath = this.createPythonScript(`
import sys
import json
from predictsolver_core.api import predict_sample

model_id = '${modelId}'
data = json.loads('''${JSON.stringify(data)}''')

result = predict_sample(model_id, data)
print(json.dumps(result))
`);

    try {
      const result = await this.runPythonScript(scriptPath);
      return JSON.parse(result);
    } catch (error) {
      this.logger.error(`Error during prediction: ${error.message}`);
      return { error: 'Prediction failed', details: error.message };
    } finally {
      this.cleanupTempFile(scriptPath);
    }
  }

  private createPythonScript(scriptContent: string): string {
    const fileName = `predictsolver_${Date.now()}_${Math.floor(Math.random() * 10000)}.py`;
    const filePath = path.join(this.tempDir, fileName);
    fs.writeFileSync(filePath, scriptContent);
    return filePath;
  }

  private runPythonScript(scriptPath: string): Promise<string> {
    return new Promise((resolve, reject) => {
      const pythonProcess = spawn(this.pythonExecutable, [scriptPath]);
      
      let result = '';
      let errorMessage = '';

      pythonProcess.stdout.on('data', (data) => {
        result += data.toString();
      });

      pythonProcess.stderr.on('data', (data) => {
        errorMessage += data.toString();
      });

      pythonProcess.on('close', (code) => {
        if (code !== 0) {
          reject(new Error(`Python process exited with code ${code}: ${errorMessage}`));
        } else {
          resolve(result.trim());
        }
      });
    });
  }

  private cleanupTempFile(filePath: string) {
    try {
      fs.unlinkSync(filePath);
    } catch (error) {
      this.logger.warn(`Failed to remove temp file ${filePath}: ${error.message}`);
    }
  }
}
