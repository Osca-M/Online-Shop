import {AbstractControl, ValidatorFn} from '@angular/forms';

export function forbiddenEmailValidator(forbiddenEmail: RegExp): ValidatorFn {
  return (control: AbstractControl): {[key: string]: any} | null => {
    const forbidden = forbiddenEmail.test(control.value);

    return forbidden ? { forbiddenEmail: {value: control.value}} : null;
  };
}
