import React, { Children, useEffect, useState } from 'react';
// import {
//   AppstoreOutlined,
//   ContainerOutlined,
//   DesktopOutlined,
//   MailOutlined,
//   MenuFoldOutlined,
//   MenuUnfoldOutlined,
//   PieChartOutlined,
// } from '@ant-design/icons';
import ProductCard from './components/ProductCard';
import { Menu, Spin } from 'antd';
import axios from 'axios';

// const products = []

function App() {
  const [collapsed, setCollapsed] = useState(false);
  const toggleCollapsed = () => {
    setCollapsed(!collapsed);
  };
  const [products, setProducts] = useState([])
  const [productId, setProductId] = useState(1)
  const [productData, setProductData] = useState(null)

  const fetchProducts = () => {
    axios.get('http://127.0.0.1:8000/catalog/').then(response => {
      console.log('response', response)
      const productsResponse = response.data
      const menuItems = [
        {
          type: "group",
          label: "Продукты",
          children: productsResponse.map(c => {
               return {label: c.name, key: c.id}}),
        }
        // getItem('Список продуктов', 'g1', productsResponse.map(c => {
        //   return {label: c.name, key: c.id}
        // }))

      ]
      setProducts(menuItems)
    })
  }

  const fetchProduct = () => {
    axios.get(`http://127.0.0.1:8000/catalog/${productId}`).then(response => {
      console.log('response', response)
      setProductData(response.data)
    })
  }

  useEffect(() => {
    fetchProducts()
  }, [])

  useEffect(() => {
    setProductData(null)
    fetchProduct()
  }, [productId])

  const onClick = (e) => {
    // console.log("click", e)
    setProductId(e.key)
  }

  return (
    <div className='flex'>
      <Menu
      onClick={onClick}
      style={{width: 256}}
      defaultSelectedKeys={['1']}
      defaultOpenKeys={['sub1']}
      mode="inline"
      theme="dark"
      inlineCollapsed={collapsed}
      items={products}
      className="h-screen overflow-scroll"/>
      <div className="mx-auto my-auto">
        {productData ? <ProductCard product={productData}/> : <Spin size='large'/>}
      </div>
    </div>
  );
};
export default App;