import axios from 'axios'
import { AuthModel, UserModel } from '.'

const API_URL = process.env.REACT_APP_API_URL

const LOGIN_URL = `${API_URL}/auth/login`
const GET_USER_BY_ACCESSTOKEN_URL = `${API_URL}/auth/user-info`

// Server should return AuthModel
export function loginPost(login: string, password: string) {
  return axios.post<AuthModel>(LOGIN_URL, {
    login,
    password,
  })
}

export function getUserByToken(token: string) {
  return axios.post<UserModel>(GET_USER_BY_ACCESSTOKEN_URL, {
    api_token: token,
  })
}
