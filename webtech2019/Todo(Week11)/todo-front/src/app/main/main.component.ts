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

  constructor(private provider: ProviderService) { }

  ngOnInit() {
    this.provider.getTaskLists().then(res => {
      this.task_lists = res;
    })
  }

  getTasks(task_list: ITaskList){
    this.provider.getTasks(task_list).then(res => {
      this.tasks = res;
      this.current_task_list = task_list;
    })
  }

  getTask(task: ITask){
    this.provider.getTask(task).then( res => {
      this.current_task = res;
    })
  }
}
