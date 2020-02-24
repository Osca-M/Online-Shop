import { Component, OnInit } from '@angular/core';
import { FormBuilder, Validators } from '@angular/forms';
import { AuthService } from '../auth.service';
import {forbiddenEmailValidator} from '../email-validator';
import {passwordValidator} from '../confirm-password-validator';

@Component({
  selector: 'app-registration',
  templateUrl: './registration.component.html',
  styleUrls: ['./registration.component.css']
})
export class RegistrationComponent implements OnInit {
  registerUserData = {}
  // registrationForm = new FormGroup({
  //   email: new FormControl(''),
  //   password: new FormControl(''),
  //   confirmPassword: new FormControl('')
  // });
  get email() {
    return this.registrationForm.get('email')
  }

  get password() {
    return this.registrationForm.get('password')
  }

  get confirmPassword() {
    return this.registrationForm.get('confirmPassword')
  }

  constructor(
    private _auth: AuthService,
    private fb: FormBuilder
  ) { }

  registrationForm = this.fb.group({
    email: ['', [Validators.required, Validators.email, forbiddenEmailValidator(/admin/)]],
    password: ['', [Validators.required, Validators.minLength(8)]],
    confirmPassword: ['']
  }, {validator: passwordValidator})

  ngOnInit() {
  }

  registerUser() {
    this._auth.registerUser(this.registerUserData)
      .subscribe(
        res => console.log(res),
        err => console.log(err)
      )
  }

}
