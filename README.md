# software-test
学习笔记:软件测试相关，测试用例，测试工具等存储

# Python环境搭建
 1.下载
   - [官方下载](https://www.python.org/)
   - [Anaconda整合版下载](https://www.anaconda.com/)
   
 2.安装
   - 根据图形化安装界面提示进行安装
   
 3.配置
   - 在环境变量中把你需要的Python路径添加进Path | ***添加PythonPath/Script可以方便pip命令运行***

# 测试工具
  ## [Selenium](http://docs.seleniumhq.org/)
  Selenium是测试自动化的家喻户晓的名字。它被认为是Web应用程序用户界面自动化测试的行业标准。
  根据"测试自动化挑战调查"显示，十分之九的测试人员中有近九位在其项目中使用或曾经使用过硒。

  对于具有编程和脚本编写经验和技能的开发人员和测试人员，Selenium提供了许多其他测试自动化工具和框架所不具备的灵活性。
  用户可以使用多种语言（例如Java，Groovy，Python，C＃，php，Ruby和Perl）编写测试脚本，这些脚本可以在多种系统环境（Windows，Mac，Linux）和浏览器（Chrome，Firefox，IE和 无头浏览器）。
  ## [Katlon Studio](https://www.katalon.com/)
  Katalon Studio是功能强大且全面的自动化解决方案，用于测试API，Web，移动和桌面应用程序测试。
  它还为这些类型的测试提供了丰富的功能集，并支持包括Windows，macOS和Linux在内的多个平台。

  利用Selenium和Appium引擎，Katalon Studio为那些难以集成和部署不同框架和库以使用Selenium和Appium的测试人员以及已经熟悉这些引擎的测试人员提供了一个独特的集成环境。

  该工具的重点包括：

 * API / Web服务，Web和移动应用程序的测试自动化的完整功能集
 * 同时支持SOAP和RESTful的API和服务测试
 * 数百个用于创建测试用例的内置关键字
 * 可用于自动化和探索性测试
 * 可以通过Katalon Store上的插件扩展测试功能，深入了解Katalon TestOps上的报告

  许可证：免费
  ## [UFT](https://www.microfocus.com/zh-cn/products/uft-one/overview)
  UFT是测试桌面，Web和移动应用程序的流行商业工具。它已扩展为包括一组用于API测试的功能。
  通过为被测目标应用程序（AUT）支持多个平台，UFT提供了一种方便的选择来测试可在台式机，Web和移动设备上运行的AUT。
  UFT为智能对象检测，基于图像的对象检测和校正提供了几种高级功能。
  
  该工具的特点包括：

 * 直观的用户界面，用于创建，执行和报告API测试
 * 支持从WADL文档生成API测试
 * 测试的动作，活动和参数可以在图表中可视化

  许可证：每年3,200美元起。
   ## [Postman](https://www.postman.com/)
   Postman是专为API测试设计的另一种自动化工具。
   用户可以在Mac，Linux，Windows上以浏览器扩展或桌面应用程序的形式安装此工具。
   它不仅在用于API测试自动化的测试人员中很流行，而且在使用该工具开发和测试API的开发人员中也很流行。
   实际上，它是用于开发和测试API的开发环境。

   该工具的一些亮点：

  * 用于设计，调试，测试，记录和发布API的综合功能集
  * 友好且易于使用的用户界面
  * 支持自动化和探索性测试
  * 接受Swagger和RAML API格式
  * 请求和应答者可以打包并与团队成员共享

   执照：商业
   ## [Apache Jmeter](https://jmeter.apache.org/)
   JMeter是设计用于测试加载和性能测量的开源工具-JMeter的两个功能是众所周知的。
   但是，该工具现在也用于API和服务测试，尤其是API性能。
   JMeter是第三种最受欢迎的测试自动化工具，在"测试自动化挑战"调查中有25％的受访者引用了JMeter的信息。

   该工具的重点包括：

  * 轻巧，具有简单易用的用户界面
  * 测试结果可以重播
  * 支持CSV文件来设置API参数的值
  * 支持与CI工具（例如Jenkins）集成。JMeter通常用作CI和DevOps工具链的一部分
  
   许可证：开源
   ## [LoadRunner](https://www.microfocus.com/en-us/products/loadrunner-professional/overview)
   LoadRunner 是一种预测系统行为和性能的负载测试工具。
   通过以模拟上千万用户实施并发负载及实时性能监测的方式来确认和查找问题，LoadRunner 能够对整个企业架构进行测试。
   通过使用LoadRunner ，企业能最大限度地缩短测试时间，优化性能和加速应用系统的发布周期。
   
   许可证：商用
   ## ["好的测试用例设计"](https://github.com/Taboo-Yu/software-test/blob/master/%E6%B5%8B%E8%AF%95%E7%94%A8%E4%BE%8B/README.md)
