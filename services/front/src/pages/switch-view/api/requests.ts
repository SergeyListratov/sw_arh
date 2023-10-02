import axios, { AxiosResponse } from "axios";
import { ISwitch } from "entities/switch";
import { QueryState, getQueryData, Response } from "shared";

export const QUERIES = {
  DETAILS: 'Switches_details_get_all'
}

const API_URL = process.env.REACT_APP_API_URL
const GET_ALL_URL = (ip: string) => `${API_URL}/switches/details/${ip}`
const DOWNLOAD_SWITCH_CONTENT_URL= (id: string) => `${API_URL}/switches/download/${id}`

export const getAll = (query: QueryState, ip: string): Promise<Response<Array<ISwitch>>> => {
  const data = getQueryData(query)
  
  return axios
  .post(GET_ALL_URL(ip), data)
  .then((d: AxiosResponse<Response<Array<ISwitch>>>) => d.data) 
}

export const downloadSwitchContent = (id: string) : Promise<AxiosResponse> => {
  return axios({
    url: DOWNLOAD_SWITCH_CONTENT_URL(id),
    method: "POST",
    responseType: 'blob'
  })
  .then((d: AxiosResponse) => d)
}