(this.webpackJsonpindra=this.webpackJsonpindra||[]).push([[0],{135:function(e,t,a){},196:function(e,t,a){e.exports=a.p+"static/media/Sandpile.090bc1a0.jpg"},197:function(e,t,a){e.exports=a.p+"static/media/sandpile_2.d38b3fb1.png"},198:function(e,t,a){e.exports=a.p+"static/media/mendelobrot_sq.875dd8b8.jpg"},237:function(e,t,a){e.exports=a(589)},585:function(e,t,a){},586:function(e,t,a){},589:function(e,t,a){"use strict";a.r(t);var n=a(0),r=a.n(n),l=a(9),o=a.n(l),c=a(103),s=a(115),i=a(46),u=a(73),d=a(615),m=a(621),p=a(622);var h=function(){return r.a.createElement(m.a,{bg:"light",expand:"lg"},r.a.createElement(m.a.Brand,{href:"/"},"INDRA"),r.a.createElement(m.a.Toggle,{"aria-controls":"basic-navbar-nav"}),r.a.createElement(m.a.Collapse,{id:"basic-navbar-nav"},r.a.createElement(p.a,{className:"mr-auto"},r.a.createElement(p.a.Link,{href:"https://gcallah.github.io/indras_net/index.html"},"ABOUT"),r.a.createElement(p.a.Link,{href:"https://github.com/gcallah/indras_net/"},"SOURCE CODE"))))};function g(e){var t=e.children;return r.a.createElement(d.a,null,r.a.createElement("link",{rel:"stylesheet",href:"//cdnjs.cloudflare.com/ajax/libs/semantic-ui/2.4.1/semantic.min.css"}),r.a.createElement(h,null),t)}g.defaultProps={children:{}};var v=g,b=a(14),f=a.n(b),E=a(33),y=a(18),k=a(19),S=a(20),O=a(21),j=a(620),D=a(616),w=a(85),N=a(223),x=a(211),C=a(54),P=a.n(C),I=(a(333),a(334),a(195)),B=a.n(I),M=function(e){Object(O.a)(a,e);var t=Object(S.a)(a);function a(){var e;Object(y.a)(this,a);for(var n=arguments.length,l=new Array(n),o=0;o<n;o++)l[o]=arguments[o];return(e=t.call.apply(t,[this].concat(l))).renderImage=function(){var t=e.props,a=t.dots,n=t.speed,l=t.autoplay,o=t.className,c=t.data,s={arrows:!1,dots:a,infinite:!0,speed:n,slidesToShow:1,slidesToScroll:1,autoplay:l,fade:!0,className:o};return r.a.createElement("div",null,r.a.createElement(B.a,s,c.map((function(e){return r.a.createElement("div",{key:e.title},r.a.createElement("img",{src:e.image,className:"rounded-circle carousel",alt:"Responsive Model","data-toggle":"tooltip","data-placement":"top",title:e.title}))}))))},e}return Object(k.a)(a,[{key:"render",value:function(){return r.a.createElement("div",null,this.renderImage())}}]),a}(n.Component);M.defaultProps={dots:!1,speed:1e3,autoplay:!1,className:"",data:[]};var F=M,R=a(196),_=a.n(R),A=a(197),V=a.n(A),T=a(198),W=a.n(T),z=(a(135),function(e){Object(O.a)(a,e);var t=Object(S.a)(a);function a(e){var n;return Object(y.a)(this,a),(n=t.call(this,e)).handleClick=function(e,t,a,n){localStorage.setItem("menu_id",e),localStorage.setItem("name",t),localStorage.setItem("source",a),localStorage.setItem("graph",n)},n.renderChooseModelProp=function(){return r.a.createElement("h1",{className:"small-header"},"Please choose a model: ")},n.state={allItems:[],loadingData:!1,apiFailed:!1,dataForCarousel:[{image:_.a,title:"by Seth Terashima"},{image:V.a,title:"by Colt Browninga"},{image:W.a,title:"by Adam Majewski"}]},n.api_server="https://indrasnet.pythonanywhere.com/",n}return Object(k.a)(a,[{key:"componentDidMount",value:function(){var e=Object(E.a)(f.a.mark((function e(){var t,a;return f.a.wrap((function(e){for(;;)switch(e.prev=e.next){case 0:return t=this.props.history,e.prev=1,this.setState({loadingData:!0}),document.title="Home",e.next=6,P.a.get("".concat(this.api_server,"models"));case 6:a=e.sent,this.setState({allItems:a.data,loadingData:!1}),e.next=13;break;case 10:e.prev=10,e.t0=e.catch(1),t.push("/errorCatching");case 13:case"end":return e.stop()}}),e,this,[[1,10]])})));return function(){return e.apply(this,arguments)}}()},{key:"render",value:function(){var e=this,t=this.state,a=t.loadingData,n=t.dataForCarousel,l=t.allItems;return t.apiFailed?r.a.createElement("h1",null,"404 Error"):a?r.a.createElement(j.a,{active:!0,inverted:!0},r.a.createElement(D.a,{size:"massive"},"Loading...")):r.a.createElement("div",{className:"container"},r.a.createElement("div",{className:"margin-bottom-80"},r.a.createElement("h1",{className:"text-left"},"Indra Agent-Based Modeling System")),r.a.createElement("div",{className:"row"},r.a.createElement("div",{className:"col-6"},this.renderChooseModelProp(),r.a.createElement(w.a,null,Object.keys(l).map((function(t){return r.a.createElement(N.a,{key:"".concat(l[t].name,"-tooltip"),placement:"right",overlay:r.a.createElement(x.a,null,l[t].doc)},r.a.createElement(s.b,{to:{pathname:"/models/props/".concat(l[t]["model ID"])},className:"text-primary w-75 p-3 list-group-item list-group-item-action link",key:l[t].name,onClick:function(){return e.handleClick(l[t]["model ID"],l[t].name,l[t].source,l[t].graph)}},l[t].name))})))),r.a.createElement("div",{className:"col-6"},r.a.createElement(F,{speed:5e3,autoplay:!0,className:"col-12",data:n}))))}}]),a}(n.Component));z.defaultProps={history:{}};var L=z,H=function(e){Object(O.a)(a,e);var t=Object(S.a)(a);function a(e){var n;return Object(y.a)(this,a),(n=t.call(this,e)).state={loadingData:!1},n}return Object(k.a)(a,[{key:"componentDidMount",value:function(){var e=Object(E.a)(f.a.mark((function e(){return f.a.wrap((function(e){for(;;)switch(e.prev=e.next){case 0:this.setState({loadingData:!0}),document.title="Indra | Work in Progress",this.setState({loadingData:!1});case 3:case"end":return e.stop()}}),e,this)})));return function(){return e.apply(this,arguments)}}()},{key:"render",value:function(){return this.state.loadingData?r.a.createElement(j.a,{active:!0,inverted:!0},r.a.createElement(D.a,{size:"massive"},"Loading...")):r.a.createElement("div",null,r.a.createElement("br",null),r.a.createElement("h1",{style:{textAlign:"center"}},"Welcome to the Indra ABM platform!"),r.a.createElement("br",null),r.a.createElement("br",null),r.a.createElement("p",null,"We will have this model running soon!"),r.a.createElement("br",null),r.a.createElement("br",null))}}]),a}(n.Component),J=a(61),q=a(86);function $(e){var t=e.label,a=e.name,n=e.type,l=e.placeholder,o=e.propChange,c=e.error;return r.a.createElement("div",{key:t,className:"form-group"},r.a.createElement("div",null,r.a.createElement("label",{htmlFor:a,className:"col-sm-4 col-md-4 col-lg-4",key:t},t," "," "),r.a.createElement("input",{id:a,type:n,className:"col-sm-2 col-md-2 col-lg-2",style:{fontSize:"15pt"},placeholder:l,onChange:o,name:a}),r.a.createElement("span",{className:"col-sm-6 col-md-6 col-lg-6",style:{color:"red",fontSize:12}},c),r.a.createElement("br",null)))}$.defaultProps={label:"",name:"",type:"",placeholder:0,propChange:function(){},error:""};var U=$;var G=function(){return r.a.createElement(j.a,{active:!0,inverted:!0},r.a.createElement(D.a,{size:"massive"},"Loading..."))},X="https://indrasnet.pythonanywhere.com/models/props/",K=function(e){Object(O.a)(a,e);var t=Object(S.a)(a);function a(e){var n;return Object(y.a)(this,a),(n=t.call(this,e)).states=function(e){var t=n.state.modelDetails;Object.keys(t).forEach((function(t){n.setState((function(a){return{modelDetails:Object(q.a)({},a.modelDetails,Object(J.a)({},t,Object(q.a)({},a.modelDetails[t],{defaultVal:e[t].val})))}}))}))},n.errors=function(){var e=n.state.modelDetails;Object.keys(e).forEach((function(e){return n.setState((function(t){return{modelDetails:Object(q.a)({},t.modelDetails,Object(J.a)({},e,Object(q.a)({},t.modelDetails[e],{errorMessage:"",disabledButton:!1})))}}))}))},n.errorSubmit=function(){var e=n.state.modelDetails,t=!1;return Object.keys(e).forEach((function(a){t=t||e[a].disabledButton})),t},n.propChanged=function(e){var t=n.state.modelDetails,a=e.target,r=a.name,l=a.value,o=n.checkValidity(r,l);t[r].disabledButton=!0,1===o?(t[r].val=parseInt(l,10),t[r].errorMessage="",t[r].disabledButton=!1,n.setState({modelDetails:t})):-1===o?(t[r].errorMessage="**Wrong Input Type",t[r].val=t[r].defaultVal,n.setState({modelDetails:t})):(t[r].errorMessage="**Please input a number between ".concat(t[r].lowval," and ").concat(t[r].hival,"."),t[r].val=t[r].defaultVal,n.setState({modelDetails:t})),n.setState({disabledButton:n.errorSubmit()})},n.checkValidity=function(e,t){var a=n.state.modelDetails;return t<=a[e].hival&&t>=a[e].lowval?"INT"===a[e].atype&&!1===!!(t%1)||"DBL"===a[e].atype?1:-1:0},n.handleSubmit=function(){var e=Object(E.a)(f.a.mark((function e(t){var a,r,l,o,c;return f.a.wrap((function(e){for(;;)switch(e.prev=e.next){case 0:return t.preventDefault(),a=n.state.modelDetails,r=n.props.history,e.prev=3,e.next=6,P.a.put(X+localStorage.getItem("menu_id"),a);case 6:l=e.sent,o=localStorage.getItem("menu_id"),n.setState({envFile:l.data}),c=n.state.envFile,localStorage.setItem("envFile",JSON.stringify(c)),r.push({pathname:"/models/menu/".concat(o.toString(10)),state:{envFile:c}}),e.next=17;break;case 14:e.prev=14,e.t0=e.catch(3),r.push("/errorCatching");case 17:case"end":return e.stop()}}),e,null,[[3,14]])})));return function(t){return e.apply(this,arguments)}}(),n.renderHeader=function(){return r.a.createElement("h1",{className:"header",style:{textAlign:"center",fontWeight:"200"}},"Please set the parameters for the ".concat(localStorage.getItem("name")," model"))},n.renderSubmitButton=function(){var e=n.state.disabledButton;return r.a.createElement("button",{type:"button",disabled:e,onClick:e?null:n.handleSubmit,className:"btn btn-primary m-2"},"Submit")},n.goback=function(){n.props.history.goBack()},n.state={modelDetails:{},loadingData:!1,disabledButton:!1,envFile:{}},n}return Object(k.a)(a,[{key:"componentDidMount",value:function(){var e=Object(E.a)(f.a.mark((function e(){var t,a;return f.a.wrap((function(e){for(;;)switch(e.prev=e.next){case 0:return t=this.props.history,e.prev=1,document.title="Indra | Property",this.setState({loadingData:!0}),e.next=6,P.a.get("".concat(X).concat(localStorage.getItem("menu_id")));case 6:a=e.sent,this.setState({modelDetails:a.data}),this.states(a.data),this.errors(a.data),this.setState({loadingData:!1}),e.next=16;break;case 13:e.prev=13,e.t0=e.catch(1),t.push("/errorCatching");case 16:case"end":return e.stop()}}),e,this,[[1,13]])})));return function(){return e.apply(this,arguments)}}()},{key:"render",value:function(){var e=this,t=this.state,a=t.loadingData,n=t.modelDetails;return a?r.a.createElement(G,null):r.a.createElement("div",null,r.a.createElement("h1",{className:"margin-top-60"}," "),this.renderHeader(),r.a.createElement("br",null),r.a.createElement("br",null),r.a.createElement("form",null,r.a.createElement("div",{className:"container"},Object.keys(n).map((function(t){return"question"in n[t]?r.a.createElement(U,{label:n[t].question,type:n[t].atype,placeholder:n[t].val,error:n[t].errorMessage,propChange:e.propChanged,name:t,key:t}):null})))),r.a.createElement("br",null),r.a.createElement("br",null),this.renderSubmitButton())}}]),a}(n.Component);K.defaultProps={history:{}};var Q=K,Y=a(57),Z=a(69),ee=a.n(Z),te=a(116);a(190);function ae(e){if(e.loadingData){var t=[],a=e.envFile.pop_hist.pops;return Object.keys(a).forEach((function(n,r){t.push({name:n,color:e.envFile.members[n].attrs.color,data:{}}),Object.keys(a[n]).forEach((function(e,l){t[r].data[e]=a[n][l]}))})),r.a.createElement("div",null,r.a.createElement(te.a,{data:t,width:"600px",height:"600px"}))}return null}ae.defaultProps={loadingData:!0,envFile:{}};var ne=ae;function re(e){var t=e.loadingData,a=e.envFile;e.id;if(t){var n=a.members,l=[];return Object.keys(n).forEach((function(e,t){l.push({name:n[e].name,color:n[e].attrs.color,data:[]}),Object.keys(n[e].members).forEach((function(a){null!==n[e].members[a].pos&&l[t].data.push(n[e].members[a].pos)}))})),r.a.createElement("div",null,r.a.createElement(te.b,{data:l,width:"600px",height:"600px"}))}return null}re.defaultProps={loadingData:!0,envFile:{},id:0};var le=re,oe=a(214),ce=a.n(oe);function se(e){var t=e.envFile;return e.loadingData?r.a.createElement(ce.a,{src:t}):null}se.defaultProps={envFile:{},loadingData:!0};var ie=se,ue=function(e){Object(O.a)(a,e);var t=Object(S.a)(a);function a(e){var n;Object(y.a)(this,a),n=t.call(this,e),ee()(Object(Y.a)(n));var r=n.props,l=r.msg,o=r.title;return n.state={msg:l,title:o},n}return Object(k.a)(a,[{key:"render",value:function(){var e=this.state,t=e.msg,a=e.title;return r.a.createElement("div",null,r.a.createElement("div",{className:"card w-50 model-status"},r.a.createElement("h5",{style:{textAlign:"center",fontSize:16},className:"card-header bg-primary text-white"},a),r.a.createElement("div",{className:"card-body overflow-auto"},r.a.createElement("pre",{className:"card-text"},t))))}}],[{key:"getDerivedStateFromProps",value:function(e,t){return e.msg!==t.msg?{msg:e.msg}:null}}]),a}(r.a.Component);ue.defaultProps={msg:"",title:""};var de=a(623),me=a(618),pe=function(e){var t=e.loadingData,a=e.code;return t?r.a.createElement(de.a,{language:"python",style:me.a},a):null};pe.defaultProps={loadingData:!0,code:""};var he=pe,ge=function(e){Object(O.a)(a,e);var t=Object(S.a)(a);function a(e){var n;return Object(y.a)(this,a),n=t.call(this,e),ee()(Object(Y.a)(n)),n.state={disabledButton:e.disabledButton,errorMessage:e.errorMessage,sendNumPeriods:e.sendNumPeriods,handleRunPeriod:e.handleRunPeriod},n}return Object(k.a)(a,[{key:"render",value:function(){var e=this.state,t=e.disabledButton,a=e.sendNumPeriods,n=e.handleRunPeriod,l=e.errorMessage;return r.a.createElement("div",null,r.a.createElement("button",{type:"button",disabled:t,onClick:t?null:a,className:"btn btn-success m-2"},"  ","Run","  ")," ",r.a.createElement("span",null,"model for")," ",r.a.createElement("input",{type:"INT",className:"from-control m-2 number-input",placeholder:"10",onChange:n})," ","periods.",r.a.createElement("span",{className:"error-message"},l))}}]),a}(r.a.Component);ge.defaultProps={disabledButton:!0,errorMessage:"",sendNumPeriods:function(){},handleRunPeriod:function(){}};var ve="https://indrasnet.pythonanywhere.com/models/menu/",be=function(e){Object(O.a)(a,e);var t=Object(S.a)(a);function a(e){var n;return Object(y.a)(this,a),(n=t.call(this,e)).viewSource=Object(E.a)(f.a.mark((function e(){var t,a,r,l;return f.a.wrap((function(e){for(;;)switch(e.prev=e.next){case 0:return e.prev=0,t=n.state.source,a=t.split("/"),r=a[a.length-1],e.next=6,P.a.get("https://raw.githubusercontent.com/gcallah/indras_net/master/models/".concat(r));case 6:return l=e.sent,e.abrupt("return",l.data);case 10:return e.prev=10,e.t0=e.catch(0),e.abrupt("return","Something has gone wrong.");case 13:case"end":return e.stop()}}),e,null,[[0,10]])}))),n.handleRunPeriod=function(e){n.setState({periodNum:e.target.value}),0===n.checkValidity(e.target.value)?n.setState({errorMessage:"**Please input an integer",disabledButton:!0}):n.setState({errorMessage:"",disabledButton:!1})},n.checkValidity=function(e){return e%1===0?1:0},n.handleClick=function(e){switch(n.setState({loadingData:!1,loadingSourceCode:!1,loadingDebugger:!1,loadingScatter:!1,loadingPopulation:!1}),n.setState({activeDisplay:e}),e){case 2:n.setState({loadingPopulation:!0});break;case 3:n.setState({loadingScatter:!0});break;case 4:n.setState({loadingDebugger:!0});break;case 5:n.setState({loadingSourceCode:!0})}},n.sendNumPeriods=Object(E.a)(f.a.mark((function e(){var t,a,r,l;return f.a.wrap((function(e){for(;;)switch(e.prev=e.next){case 0:return t=n.state,a=t.periodNum,r=t.envFile,n.setState({loadingData:!0}),e.prev=2,e.next=5,P.a.put("".concat(ve,"run/").concat(String(a)),r,a);case 5:return l=e.sent,n.setState({envFile:l.data,loadingData:!1,msg:l.data.user.user_msgs}),e.abrupt("return",!0);case 10:return e.prev=10,e.t0=e.catch(2),e.abrupt("return",!1);case 13:case"end":return e.stop()}}),e,null,[[2,10]])}))),n.renderHeader=function(){var e=n.state.name;return r.a.createElement("h1",{className:"header"},e)},n.MenuItem=function(e,t,a,l){var o=localStorage.getItem("graph"),c=n.state.activeDisplay;return r.a.createElement(w.a.Item,{className:"w-50 p-3 list-group-item list-group-item-action",as:"li",active:c===t,disabled:3===t&&"line"===o||2===t&&"scatter"===o,key:l,onClick:function(){return n.handleClick(t)}},a)},n.renderMenuItem=function(){var e=n.state,t=e.envFile,a=e.loadingDebugger,l=e.loadingSourceCode,o=e.sourceCode,c=e.loadingPopulation,s=e.loadingScatter;return r.a.createElement("div",null,r.a.createElement(ie,{loadingData:a,envFile:t}),r.a.createElement(he,{loadingData:l,code:o}),r.a.createElement(ne,{loadingData:c,envFile:t}),r.a.createElement(le,{loadingData:s,envFile:t}))},n.renderMapItem=function(){var e=n.state.menu;return r.a.createElement("div",{className:"row margin-bottom-80"},r.a.createElement("div",{className:"col w-25"},r.a.createElement(w.a,null,Object.keys(e).map((function(t,a){return e[t].id>1?n.MenuItem(a,e[t].id,e[t].question,e[t].func):null})))))},ee()(Object(Y.a)(n)),n.state={menu:{},loadingData:!0,envFile:{},source:"",periodNum:10,errorMessage:"",disabledButton:!1,loadingSourceCode:!1,loadingDebugger:!1,loadingPopulation:!1,loadingScatter:!1,activeDisplay:null},n}return Object(k.a)(a,[{key:"componentDidMount",value:function(){var e=Object(E.a)(f.a.mark((function e(){var t,a;return f.a.wrap((function(e){for(;;)switch(e.prev=e.next){case 0:return e.prev=0,document.title="Indra | Menu",e.next=4,P.a.get(ve);case 4:t=e.sent,this.setState({menu:t.data,name:localStorage.getItem("name"),source:localStorage.getItem("source"),envFile:JSON.parse(localStorage.getItem("envFile")),msg:JSON.parse(localStorage.getItem("envFile")).user.user_msgs,loadingData:!1}),e.next=11;break;case 8:return e.prev=8,e.t0=e.catch(0),e.abrupt("return",!1);case 11:return"scatter"===localStorage.getItem("graph")?this.setState({loadingScatter:!0,activeDisplay:3}):this.setState({loadingPopulation:!0,activeDisplay:2}),e.prev=13,e.next=16,this.viewSource();case 16:a=e.sent,this.setState({sourceCode:a}),e.next=23;break;case 20:return e.prev=20,e.t1=e.catch(13),e.abrupt("return",!1);case 23:return e.abrupt("return",!0);case 24:case"end":return e.stop()}}),e,this,[[0,8],[13,20]])})));return function(){return e.apply(this,arguments)}}()},{key:"render",value:function(){var e=this.state,t=e.loadingData,a=e.msg,n=e.disabledButton,l=e.errorMessage;return t?r.a.createElement(G,null):r.a.createElement("div",null,this.renderHeader(),r.a.createElement("div",null,r.a.createElement(ue,{title:"Model Status",msg:a,ref:this.modelStatusBoxElement})),r.a.createElement("ul",{className:"list-group"},r.a.createElement("div",{className:"row"},r.a.createElement("div",null,r.a.createElement(ge,{disabledButton:n,errorMessage:l,sendNumPeriods:this.sendNumPeriods,handleRunPeriod:this.handleRunPeriod}),r.a.createElement("h3",{className:"margin-top-50 mb-4"},"Model Analysis:"))),this.renderMapItem()),this.renderMenuItem())}}]),a}(n.Component);be.defaultProps={history:{}};var fe=be,Ee=(a(585),function(e){var t=e.code,a=e.children;return r.a.createElement(i.a,{render:function(e){var n=e.staticContext;return n&&(n.status=t),a}})});Ee.defaultProps={code:0,children:{}};var ye=function(){return r.a.createElement(Ee,{code:404},r.a.createElement("div",{className:"NotFoundPage"},r.a.createElement("h1",null,"Oops!"),r.a.createElement("div",null,"Page not found."),r.a.createElement("div",{className:"action"},r.a.createElement("a",{className:"btn btn-primary",href:"/"},"Guide me to the right path!"))))},ke=function(e){Object(O.a)(a,e);var t=Object(S.a)(a);function a(e){var n;return Object(y.a)(this,a),(n=t.call(this,e)).state={loadingData:!1},n}return Object(k.a)(a,[{key:"componentDidMount",value:function(){var e=Object(E.a)(f.a.mark((function e(){return f.a.wrap((function(e){for(;;)switch(e.prev=e.next){case 0:this.setState({loadingData:!0}),document.title="Indra | Work in Progress",this.setState({loadingData:!1});case 3:case"end":return e.stop()}}),e,this)})));return function(){return e.apply(this,arguments)}}()},{key:"render",value:function(){return this.state.loadingData?r.a.createElement(j.a,{active:!0,inverted:!0},r.a.createElement(D.a,{size:"massive"},"Loading...")):r.a.createElement("div",null,r.a.createElement("br",null),r.a.createElement("h1",{style:{textAlign:"center"}},"Indra ABM platform"),r.a.createElement("br",null),r.a.createElement("br",null),r.a.createElement("p",null,"We are encountering some problems with the API server. We will have this model running soon!"),r.a.createElement("br",null),r.a.createElement("br",null))}}]),a}(n.Component);function Se(){var e=Object(c.a)(["\n  background: ",';\n  width: 100vw;\n  min-height: 100vh;\n  font-family: -apple-stem, BlinkMacSystemFont, "Segoe UI", "Roboto", "Oxygen";\n  h1 {\n    color: ',";\n  }\n"]);return Se=function(){return e},e}var Oe=Object(u.b)("div")(Se(),(function(e){return e.theme.background}),(function(e){return e.theme.body}));function je(){return r.a.createElement(i.c,null,r.a.createElement(i.a,{exact:!0,path:"/",component:L}),r.a.createElement(i.a,{exact:!0,path:"/wip",component:H}),r.a.createElement(i.a,{exact:!0,path:"/models/props/:id",component:Q}),r.a.createElement(i.a,{exact:!0,path:"/models/menu/:id",component:fe}),r.a.createElement(i.a,{exact:!0,path:"/errorCatching",component:ke}),r.a.createElement(i.a,{component:ye}))}var De=Object(u.c)((function(){return r.a.createElement(Oe,null,r.a.createElement(s.a,null,r.a.createElement(v,null,r.a.createElement(je,null))))})),we=(a(586),a(587),a(588),a(224)),Ne=a(226),xe=a(619),Ce=a(44),Pe=a(87),Ie=a.n(Pe),Be=Ie()("mode",{light:"#fafafa",dark:"#222"}),Me=Ie()("mode",{light:"#000",dark:"#fff"});Ie()("mode",{light:"#222",dark:"#eee"}),Ie()("mode",{light:"#eee",dark:"#222"});function Fe(){var e=Object(c.a)(["\n    background-color: ",";\n    color: ",";\n  "]);return Fe=function(){return e},e}var Re=r.a.createContext(),_e=Object(Ce.a)((function(e){return{root:{width:42,height:26,padding:0,margin:e.spacing(1)},switchBase:{padding:1,"&$checked":{transform:"translateX(16px)",color:e.palette.common.white,"& + $track":{backgroundColor:"#060606",opacity:1,border:"none"}},"&$focusVisible $thumb":{color:"#060606",border:"6px solid #fff"}},thumb:{width:24,height:24},track:{borderRadius:13,border:"1px solid ".concat(e.palette.grey[400]),backgroundColor:e.palette.grey[50],opacity:1,transition:e.transitions.create(["background-color","border"])},checked:{},focusVisible:{}}}))((function(e){var t=e.classes,a=Object(Ne.a)(e,["classes"]);return r.a.createElement(xe.a,Object.assign({focusVisibleClassName:t.focusVisible,disableRipple:!0,classes:{root:t.root,switchBase:t.switchBase,thumb:t.thumb,track:t.track,checked:t.checked}},a))})),Ae=function(e){var t=e.children,a=r.a.useState({mode:"light",checkedB:!0}),n=Object(we.a)(a,2),l=n[0],o=n[1],c=u.b.div(Fe(),Be,Me),s=function(e){return function(t){var a="light"===l.mode?"dark":"light";o(Object(J.a)({mode:a},e,t.target.checked))}};return r.a.createElement(Re.Provider,{value:{toggle:s}},r.a.createElement(u.a,{theme:{mode:l.mode}},r.a.createElement(c,null,r.a.createElement(_e,{checked:l.checkedB,onChange:s("checkedB"),value:"checkedB"}),t)))};o.a.render(r.a.createElement(Ae,null,r.a.createElement(De,null)),document.getElementById("root"))}},[[237,1,2]]]);
//# sourceMappingURL=main.e6eb749e.chunk.js.map