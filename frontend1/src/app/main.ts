import { bootstrapApplication } from '@angular/platform-browser';
import { AppComponent } from './app.component'; // ⬅️ Убрал лишний 'app/'
import { provideRouter } from '@angular/router';
import { routes } from './app.routes';          // ⬅️ Убрал лишний 'app/'
import { provideReactiveForms } from '@angular/forms'; // об этом ниже



bootstrapApplication(AppComponent, {
  providers: [
    provideRouter(routes),
    provideReactiveForms(), 
  ]
}).catch(err => console.error(err));
