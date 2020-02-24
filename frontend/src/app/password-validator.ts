import { AbstractControl } from '@angular/forms';

export function forbiddenEmailValidator(control: AbstractControl): {[key: string]: any} | null {
  const forbidden = /admin/.test(control.value);

  return forbidden ? { forbiddenEmail: {value: control.value}} : null;
}
