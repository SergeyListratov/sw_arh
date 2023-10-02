import { GridModel } from "shared"

export interface ISwitch extends GridModel {
  ip: string
  model: string
  serial: string
  created_on: Date
}

export interface ISwitchDetails extends GridModel {
  model: string
  serial: string
  created_on: Date
}
