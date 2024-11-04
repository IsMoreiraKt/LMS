FROM node:16 AS build

WORKDIR /lda_frontend
COPY lda_frontend/package*.json ./
RUN npm install

COPY lda_frontend .
RUN npm run build



FROM nginx:alpine

COPY --from=build /lda_frontend/dist /usr/share/nginx/html

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]