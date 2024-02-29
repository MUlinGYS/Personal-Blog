
export interface User {
  account: string;
  password: string;
}
import apiClient from './jsonserver';

export const getUsers = () => {
  return apiClient.get('/users')
    .then(response => response.data as User[]);
};