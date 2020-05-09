/* eslint-disable */
import { Model } from 'vue-mc';

export default class Ddjj extends Model {
  // Default attributes that define the "empty" state.
  defaults() {
    return {
      id: null,
      email: '',
      username: '',
      password: '',
      confirm_password: '',
      first_name: '',
      last_name: '',
    };
  }

}
