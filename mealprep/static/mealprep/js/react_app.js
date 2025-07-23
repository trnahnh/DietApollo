const e = React.createElement;
function CalorieApp() {
  const [data, setData] = React.useState({protein:0, carbs:0, calories:0});
  const handleChange = k => e => setData({...data, [k]: parseFloat(e.target.value) });
  return e("div", null,
    e("input", {placeholder:"Protein", onChange:handleChange("protein")}),
    e("input", {placeholder:"Carbs", onChange:handleChange("carbs")}),
    e("input", {placeholder:"Calories", onChange:handleChange("calories")}),
    e("p", null, `Protein: ${data.protein}`),
    e("p", null, `Carbs: ${data.carbs}`),
    e("p", null, `Calories: ${data.calories}`)
  );
}
ReactDOM.render(e(CalorieApp), document.getElementById("calorie-app"));
