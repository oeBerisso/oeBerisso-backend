import axios from 'axios';

const BASE_URL = process.env.VUE_APP_BACKEND_URL || '/api';

export default (data) => axios.create({
  baseURL: BASE_URL,
  headers: {
    'Content-Type': 'Application/Json',
    'Access-Control-Allow-Origin': '*',
  },
})(data)
  .then((res) => {
    if (res.status < 300) {
      return res;
    }
    throw res;
  })
  .catch((err) => {
    throw err;
  });
