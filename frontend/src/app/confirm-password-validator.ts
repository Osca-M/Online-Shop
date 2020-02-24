import { AbstractControl } from '@angular/forms';

export function passwordValidator(control: AbstractControl): {[key: string]: boolean} | null {
  const password = control.get('password');
  const confirmPassword = control.get('confirmPassword');

  return password && confirmPassword && password.value !== confirmPassword.value ?
    { misMatch: true } :
    null;
}
