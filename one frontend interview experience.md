## questions unsolved

### implementation:
```
jsonp
basic idea:
function jsonp(url, callback:function||string){
document.createElement(script)
script.url = url
if(typeof callback === 'String') {

} else {
}
}
batch async request
function batchReqs(urls)
{
  let promises = [];
  for(url of urls) {
    promises.push(new Promises((resolve, reject) => {
      fetch(url)  
    }))
  }
  Promise.all(promises).then((values)=>{
  
  }).catch(error)
}
step2. only print successed responses
```

### short answer questions:

```
1. middleware in express; how to process req res
2. cors
3. react-router: difference between hash and history
4. ajax process; other funciton except fetch; is fetch original js funciton

```

## some other questions
```
1. webpack loader plugin
2. CI/CD 
3. redux how you think about redux
4. did you plan to replace redux with context api
5. hooks 
6. react what's the react
7. cross origin 
8. ...
```

