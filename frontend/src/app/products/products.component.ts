import { Component, OnInit } from '@angular/core';
import { ProductsService } from '../products.service';

@Component({
  selector: 'app-products',
  templateUrl: './products.component.html',
  styleUrls: ['./products.component.css']
})
export class ProductsComponent implements OnInit {

  products = []
  constructor(
    private _productService: ProductsService
  ) { }

  ngOnInit() {
    this._productService.listProducts()
      .subscribe(
        res => this.products = res,
        err => console.log(err)
      )
  }

}
