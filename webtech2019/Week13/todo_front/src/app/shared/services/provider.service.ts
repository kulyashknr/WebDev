import { Injectable, EventEmitter } from '@angular/core';
import {MainService} from "./main.service";
import {HttpClient} from "@angular/common/http";
import {ITaskList, ITask, IAuthResponse, IUser} from "../models/models";

@Injectable({
  providedIn: 'root'
})

export class ProviderService extends MainService{

  constructor(http: HttpClient) {
    super(http);
  }

  getTaskLists(): Promise<ITaskList[]>{
    return this.get(`http://localhost:8000/api/task_list/`, {});
  }

  createTaskList(name: any): Promise<ITaskList>{
    return this.post(`http://localhost:8000/api/task_list/`, {
      name: name
    })
  }

  getTaskList(task_list: ITaskList): Promise<ITaskList>{
    return this.get(`http://localhost:8000/api/task_list/${task_list.id}/`, {})
  }

  updateTaskList(task_list: ITaskList){
    return this.put(`http://localhost:8000/api/task_list/${task_list.id}/`, {
      name: task_list.name
    })
  }

  deleteTaskList(id: number) {
    return this.delet(`http://localhost:8000/api/task_list/${id}/`, {});
  }

  getTasks(task_list: ITaskList): Promise<ITask[]>{
    return this.get(`http://localhost:8000/api/task_list/${task_list.id}/tasks/`, {})
  }

  createTask(task_list:ITaskList, name: any, created_at: any, due_on: any, status: any): Promise<ITask>{
    return this.post(`http://localhost:8000/api/task_list/${task_list.id}/tasks/`, {
      name: name,
      created_at: created_at,
      due_on: due_on,
      status: status
    })
  }

  getTask(task: ITask): Promise<ITask>{
    return this.get(`http://localhost:8000/api/tasks/${task.id}/`, {})
  }

  updateTask(task: ITask){
    return this.put(`http://localhost:8000/api/tasks/${task.id}/`, {
      name: task.name,
      created_at: task.created_at,
      due_on: task.due_on,
      status: task.status
    })
  }

  deleteTask(id: number){
    return this.delet(`http://localhost:8000/api/tasks/${id}/`, {})
  }

  login(username: any, password: any): Promise<IAuthResponse>{
    return this.post('http://localhost:8000/api/login/', {
      username: username,
      password: password
    })
  }

  register(username: any, password: any, email: any): Promise<IUser>{
    return this.post('http://localhost:8000/api/register/', {
      username: username,
      password: password,
      email: email
    })
  }
}
