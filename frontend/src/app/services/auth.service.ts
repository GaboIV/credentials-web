import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Router } from '@angular/router';
import { environment } from '../../environments/environment';

@Injectable({
  providedIn: 'root'
})
export class AuthService {
  private apiUrl = environment.apiUrl;

  constructor(private http: HttpClient, private router: Router) {}

  login(credentials: { username: string, password: string }) {
    return this.http.post<{ access_token: string }>(`${this.apiUrl}/auth/login`, credentials)
      .subscribe({
        next: (response) => {
          localStorage.setItem('token', response.access_token);
          this.router.navigate(['/']);
        },
        error: (err) => {
          console.error('Error en el login:', err);
        }
      });
  }

  isAuthenticated(): boolean {
    return !!localStorage.getItem('token');
  }

  logout() {
    localStorage.removeItem('token');
    this.router.navigate(['/login']);
  }
}
