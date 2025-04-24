import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-courses',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './courses.component.html',
  styleUrls: ['./courses.component.css']
})
export class CoursesComponent {
  courses = [
    {
      title: 'JavaScript for Beginners',
      description: 'Learn JavaScript from scratch with hands-on projects.',
      price: 49.99
    },
    {
      title: 'Advanced TypeScript',
      description: 'Master TypeScript with real-world examples.',
      price: 59.99
    },
    {
      title: 'Angular Crash Course',
      description: 'Build dynamic web apps using Angular.',
      price: 69.99
    },
    {
      title: 'React Essentials',
      description: 'Get started with React and build modern UI.',
      price: 59.99
    },
    {
      title: 'Python for Data Science',
      description: 'Analyze data with Python and Pandas.',
      price: 79.99
    },
    {
      title: 'Full-Stack Web Development',
      description: 'Become a full-stack developer using MERN stack.',
      price: 99.99
    },
    {
      title: 'C# and .NET Fundamentals',
      description: 'Intro to C# and building apps with .NET.',
      price: 69.99
    },
    {
      title: 'Rust Programming Basics',
      description: 'Explore Rust for systems programming.',
      price: 54.99
    },
    {
      title: 'Java & Spring Boot',
      description: 'Create powerful backend apps with Spring.',
      price: 89.99
    },
    {
      title: 'Kotlin for Android',
      description: 'Develop Android apps with Kotlin.',
      price: 74.99
    }
  ];
}
