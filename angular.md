# Angular

### Use ng-bind directive to avoid flashing

    <h1 ng-bind="item.title"></h1>

### One-time data binding

    <p ng-bind="::item.description"></p>
    
### Cause model to only update on blur (loss of focus)

    <input type="text" ng-model="item.value" ng-model-options="{updateOn: 'blur'}" />
    
### Set model update delay on last activity

Below sets a 500 ms delay before updating the model:

    <input type="text" ng-model="item.value" ng-model-options="{debounce: 500}" />
    
Delay can also be selectively added upon other events, such as on blur and the default behavior:

    <input type="text" ng-model="item.value" ng-model-options="{updateOn: 'default blur', debounce: {default: 500, blur 100}}" />
