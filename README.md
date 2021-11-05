#### Javascript calling the function:
```javascript
import "./styles.css";
import { useState } from "react";

export default function App() {
  const [age, setAge] = useState(0);
  const [classification, setClassification] = useState("");
  const submit = async (e) => {
    e.preventDefault();
    fetch(
      "https://r0yq9rcnu0.execute-api.eu-west-1.amazonaws.com/stepFunctionsLambda",
      {
        method: "POST",
        body: JSON.stringify({ age: parseInt(age, 10) })
      }
    )
      .then((res) => res.json())
      .then((json) => {
        return json.executionArn;
      })
      .then((arn) => {
        alert(arn);
        fetch(
          `https://r0yq9rcnu0.execute-api.eu-west-1.amazonaws.com/executionStatus?executionArn=${arn}`
        )
          .then((response) => {
            return response.json();
          })
          .then((res) => {
            alert(res.status);
            setClassification(JSON.parse(res.output).classification);
          });
      });
  };

  return (
    <div className="App">
      <h1>Age Sorter</h1>
      <h2>Start editing to see some magic happen!</h2>
      <form onSubmit={submit}>
        <label>
          Age:
          <input
            type="text"
            name="age"
            onChange={(e) => setAge(e.target.value)}
          />
        </label>
        <input type="submit" />
      </form>
      {classification && <div>{classification}</div>}
    </div>
  );
}

```
Had some issues with asynchronous requests. WIP. 

https://codesandbox.io/s/aws-step-functions-lambda-functions-kfkfk?file=/src/App.js:0-1396

API gateway:

<img width="1186" alt="Screenshot 2021-11-05 at 06 09 05" src="https://user-images.githubusercontent.com/27693622/140466159-e3760b45-0be9-41b1-b121-89bdd583cbdc.png">
