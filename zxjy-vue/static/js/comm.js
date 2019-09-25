import axios from 'axios'

export function send (url, type, data) {
  var d = new FormData()
  for (var key in data) {
    d.append(key, data[key])
  }
  return axios({
    url: url,
    data: d,
    method: type
  })
}
