# Spring Cloud 的服务发现框架——Eureka
- 服务注册 register
- 服务续约 Renew
- 获取注册列表信息 Fetch Registries
- 服务下线 Cancel
- 服务剔除 Eviction

# 负载均衡
- Ribbon: 面向客户端
    - RoundRobinRule: 询问策略、最多10轮、没有找到返回null
    - RandomRule: 随即策略
    - RetryRule: 重试策略，指定时间内重试，默认时间为500毫秒
- Nginx: 集中式负载均衡

# Open Feign
- 内置Ribbon
- 服务间用映射的方式无缝开发

# Hystrix
- 服务的熔断和降级

# Zuul 网关



## SpringBoot 注解

```java
@SpringBootConfiguration        // springboot 的配置
    @Configuration              // spring 配置类
    @Component                  // spring 的一个组件

@EnableAutoConfiguration        // 自动配置
    @AutoConfigurationPackage   // 自动配置包
    @Import(AutoConfigurationPackages.Register.class)   // 导入选择器
    
```



