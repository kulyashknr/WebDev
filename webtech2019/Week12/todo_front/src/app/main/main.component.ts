import { Component, OnInit } from '@angular/core';
import { ProviderService } from "../shared/services/provider.service";
import { ITaskList, ITask } from "../shared/models/models";

@Component({
  selector: 'app-main',
  templateUrl: './main.component.html',
  styleUrls: ['./main.component.css']
})

export class MainComponent implements OnInit {
  public task_lists: ITaskList[] = [];
  public tasks: ITask[] = [];
  public current_task_list: ITaskList;
  public current_task: ITask;
  public mode: String='';

  public task_list_name: any='';

  public task_name: any='';
  public task_created_at: any='';
  public task_due_on: any='';
  public task_status: any='';

  public default_date = '0000-00-00T00:00:0Z';

  constructor(private provider: ProviderService) { }

  ngOnInit() {
    this.provider.getTaskLists().then(res => {
      this.task_lists = res;
    })
  }

  getTaskList(task_list: ITaskList){
    this.provider.getTaskList(task_list).then(res => {
      this.current_task_list = res;
    })
    this.changeMode('update_list');
  }

  createTaskList(){
    this.changeMode('create_list');
    if(this.task_list_name != '') {
      this.provider.createTaskList(this.task_list_name).then(res => {
        this.task_lists.push(res)
        this.task_list_name = ''
      })
    }
  }

  updateTaskList(){
    if(this.task_list_name != ''){
      this.current_task_list.name = this.task_list_name;
      this.provider.updateTaskList(this.current_task_list).then(res => {
        for (let i = 0; i < this.task_lists.length; i++){
          if (this.task_lists[i].id == this.current_task_list.id){
            this.task_lists[i].name = this.task_list_name;
          }
        }
        this.task_list_name = '';
      })
    }
  }

  deleteTaskList(id: number){
    this.provider.deleteTaskList(id).then(res => {
      for( let i = 0; i < this.task_lists.length; i++){
        if ( this.task_lists[i].id === id) {
          this.task_lists.splice(i, 1);
        }
      }
    })
  }

  getTasks(task_lists: ITaskList){
    this.changeMode('tasks');
    this.provider.getTasks(task_lists).then(res => {
      this.tasks = res;
      this.current_task_list = task_lists;
    })
  }

  createTask(task_list: ITaskList){
    this.changeMode('create_task');
    if(this.task_name != '' || this.task_created_at != '' || this.task_due_on != '' || this.task_status != '') {
      this.provider.createTask(task_list, this.task_name, this.task_created_at, this.task_due_on, this.task_status).then(res => {
        this.mode = 'tasks';
        this.tasks.push(res);
        this.task_name = '';
        this.task_created_at = '';
        this.task_due_on = '';
        this.task_status = ''
      })
    }
  }

  getTask(task: ITask){
    this.provider.getTask(task).then( res => {
      this.changeMode('task')
      this.current_task = res;
    })
  }

  updateTask(task: ITask){
    this.changeMode('update_task');
    this.provider.updateTask(task).then(res => {
      this.changeMode('task')
      this.task_name = '';
      this.task_created_at = '';
      this.task_due_on = '';
      this.task_status = '';
    })
  }

  deleteTask(id: number){
    this.changeMode('tasks')
    this.provider.deleteTask(id).then(res => {
      for( let i = 0; i < this.tasks.length; i++){
        if ( this.tasks[i].id === id) {
          this.tasks.splice(i, 1);
        }
      }
    })
  }

  changeMode(mode: String){
    this.mode = mode;
  }
}
