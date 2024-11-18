import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';
import { environment } from '../../environments/environment';
import { Credential } from '../models/Credential';

@Injectable({
  providedIn: 'root'
})
export class CredentialsService {

  private apiUrl = environment.apiUrl;

  constructor(private http: HttpClient) { }

  getCredentials(): Observable<{ credentials: Credential[] }> {
    const token = localStorage.getItem('token');
    const headers = new HttpHeaders({ 'Authorization': `Bearer ${token}` });
    return this.http.get<{ credentials: Credential[] }>(`${this.apiUrl}/auth/get_credentials`, { headers });
  }
}
