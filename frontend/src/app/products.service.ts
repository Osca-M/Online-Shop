import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class ProductsService {

  private _listproductsurl = 'http://localhost:8000/products/list-products';
  constructor(
    private http: HttpClient
  ) { }

  listProducts() {
    return this.http.get<any>(this._listproductsurl)
  }

}
