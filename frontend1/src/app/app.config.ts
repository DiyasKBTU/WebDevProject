import { ApplicationConfig } from '@angular/core';
import { provideRouter } from '@angular/router';
import { routes } from './app.routes'; // <-- добавим маршруты из отдельного файла

export const appConfig: ApplicationConfig = {
  providers: [
    provideRouter(routes)
  ]
};
