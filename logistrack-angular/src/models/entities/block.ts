import {Driver} from "./driver";

export interface Block {
  id: string;
  creation_date: string;
  driver: Driver;
}
