# Angular

### Use ng-bind directive to avoid flashing

    <h1 ng-bind="item.title"></h1>

### One-time data binding

    <p ng-bind="::item.description"></p>
    
### Cause model to only update on blur (loss of focus)

    <input type="text" ng-model="item.value" ng-model-options="{updateOn: 'blur'}" />
