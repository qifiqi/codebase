import san from "san";
import { router } from "san-router";
import App from "./view/s-transition.san";

router.add({ rule: '/', Component: App, target: '#app' });
router.start();
console.log('Server starts.');
